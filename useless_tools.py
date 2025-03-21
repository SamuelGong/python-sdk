from noise_tools import aws, x


use_less_tools = []
# https://github.com/modelcontextprotocol/servers?tab=readme-ov-file
# Community Servers
tools_list = [
    aws.get_aws_tools(),
    x.list_tools()
]


for tools in tools_list:
    for tool in tools:
        use_less_tools.append({
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            }
        })
