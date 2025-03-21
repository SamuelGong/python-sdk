import asyncio
import os
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from anthropic import Anthropic
from dotenv import load_dotenv

from openai import OpenAI
import httpx
import json

load_dotenv()  # load environment variables from .env


class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.anthropic = Anthropic()

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")

        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

        # List available tools
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def process_query(self, query: str) -> str:
        """Process a query using Claude and available tools"""
        model = "ep-20250212105505-5zlbx"
        messages = [
            {
                "role": "user",
                "content": query
            }
        ]

        response = await self.session.list_tools()

        # available_tools = [{
        #     "name": tool.name,
        #     "description": tool.description,
        #     "input_schema": tool.inputSchema
        # } for tool in response.tools]
        # reference: https://platform.openai.com/docs/api-reference/chat/create
        available_tools = [{
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            }
        } for tool in response.tools]
        # Available tools: [{'type': 'function', 'function': {'name': 'get_alerts', 'description': 'Get weather alerts for a US state.\n\n    Args:\n        state: Two-letter US state code (e.g. CA, NY)\n    ', 'input_schema': {'properties': {'state': {'title': 'State', 'type': 'string'}}, 'required': ['state'], 'title': 'get_alertsArguments', 'type': 'object'}}}, {'type': 'function', 'function': {'name': 'get_forecast', 'description': 'Get weather forecast for a location.\n\n    Args:\n        latitude: Latitude of the location\n        longitude: Longitude of the location\n    ', 'input_schema': {'properties': {'latitude': {'title': 'Latitude', 'type': 'number'}, 'longitude': {'title': 'Longitude', 'type': 'number'}}, 'required': ['latitude', 'longitude'], 'title': 'get_forecastArguments', 'type': 'object'}}}]

        # Initial Claude API call
        # print(f"\nAvailable tools: {available_tools}")
        # response = self.anthropic.messages.create(
        #     model="claude-3-5-sonnet-20241022",
        #     max_tokens=1000,
        #     messages=messages,
        #     tools=available_tools
        # )
        endpoint = OpenAI(
            api_key=os.getenv("ARK_API_KEY"),
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            http_client=httpx.Client(
                verify=False  # important for company use
            )
        )
        payload = {
            "model": model,
            "messages": messages,
            "tools": available_tools
        }
        completion = endpoint.chat.completions.create(**payload)
        # response = completion.choices[0].message.content
        # print(f"\nMessage: {completion.choices[0]}")
        # exit()
        # print(f"Response: {response}")

        # Process response and handle tool calls
        tool_results = []
        final_text = []
        # for content in response.content:
        if True:
            choice = completion.choices[0]

            # if content.type == 'text':
            if choice.finish_reason == 'stop':
                # final_text.append(content.text)
                final_text.append(choice.message.content)
            # elif content.type == 'tool_use':
            elif choice.finish_reason == "tool_calls":
                # tool_name = content.name
                # tool_args = content.input
                message = choice.message
                tool_call = message.tool_calls[0]
                tool_call_id = tool_call.id
                function = tool_call.function
                tool_name = function.name
                tool_args = function.arguments

                # necessary for doubao 1.5 which is not fully aligned
                tool_args = json.loads(tool_args)

                # Execute tool call
                tool_call_result = await self.session.call_tool(tool_name, tool_args)
                # print(f"\nResult: {tool_call_result}")
                # print(type(tool_call_result.content[0]))
                # exit(0)

                tool_results.append({"call": tool_name, "result": tool_call_result})
                final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")

                # Continue conversation with tool results
                # if hasattr(content, 'text') and content.text:
                #     messages.append({
                #         "role": "assistant",
                #         "content": content.text
                #     })
                # messages.append({
                #     "role": "user",
                #     "content": result.content
                # })
                messages.append({
                    "role": "assistant",
                    "content": message.content,
                    "tool_calls": [{
                        "function": {"name": tool_name, "arguments": json.dumps(tool_args)},
                        "id": tool_call_id,
                        "type": "function"
                    }]
                })

                # Get next response from Claude
                # response = self.anthropic.messages.create(
                #     model="claude-3-5-sonnet-20241022",
                #     max_tokens=1000,
                #     messages=messages,
                # )
                # final_text.append(response.content[0].text)
                messages.append({
                    "role": "tool",
                    "name": tool_name,
                    "tool_call_id": tool_call_id,
                    "content": tool_call_result.content[0].text
                })
                payload = {
                    "model": model,
                    "messages": messages,
                    "tools": available_tools
                }
                completion = endpoint.chat.completions.create(**payload)
                final_text.append(completion.choices[0].message.content)


        return "\n".join(final_text)

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()

                if query.lower() == 'quit':
                    break

                response = await self.process_query(query)
                print("\n" + response)

            except Exception as e:
                print(f"\nError: {str(e)}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()


async def main():
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_server_script>")
        sys.exit(1)

    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()


if __name__ == "__main__":
    import sys

    asyncio.run(main())
