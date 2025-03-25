from noise_tools import (aws, x, git, time, redis, discord,
                         sqlite, brave_search, google_map, docker)


use_less_tools = []
# https://github.com/modelcontextprotocol/servers?tab=readme-ov-file
# Community Servers
tools_list = [
    aws.get_aws_tools(),
    x.list_tools(),
    git.list_tools(),
    time.list_tools(),
    sqlite.list_tools(),
    brave_search.list_tools(),
    google_map.list_tools(),
    redis.list_tools(),
    discord.list_tools(),
    docker.list_tools()
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
print(f"Number of useless tools: {len(use_less_tools)}")
