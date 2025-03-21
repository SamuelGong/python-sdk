from noise_tools import aws

use_less_tools = []

tools = aws.get_aws_tools()
for tool in tools:
    use_less_tools.append({
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        }
    })