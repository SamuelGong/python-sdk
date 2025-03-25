# https://github.com/modelcontextprotocol/servers/blob/main/src/brave-search
from mcp.types import (
    Tool,
)


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="brave_web_search",
            description="Performs a web search using the Brave Search API, ideal for general queries, news, articles, and online content."
                        "Use this for broad information gathering, recent events, or when you need diverse web sources. "
                        "Supports pagination, content filtering, and freshness controls. "
                        "Maximum 20 results per request, with offset for pagination. ",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query (max 400 chars, 50 words)"
                    },
                    "count": {
                        "type": "number",
                        "description": "Number of results (1-20, default 10)",
                        "default": 10
                    },
                    "offset": {
                        "type": "number",
                        "description": "Pagination offset (max 9, default 0)",
                        "default": 0
                    },
                },
                "required": ["query"],
            }
        ),
        Tool(
            name="brave_local_search",
            description="Searches for local businesses and places using Brave's Local Search API. "
                        "Best for queries related to physical locations, businesses, restaurants, services, etc. "
                        "Returns detailed information including:\n"
                        "- Business names and addresses\n"
                        "- Ratings and review counts\n"
                        "- Phone numbers and opening hours\n"
                        "Use this when the query implies 'near me' or mentions specific locations. "
                        "Automatically falls back to web search if no local results are found.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Local search query (e.g. 'pizza near Central Park')"
                    },
                    "count": {
                        "type": "number",
                        "description": "Number of results (1-20, default 5)",
                        "default": 5
                    },
                },
                "required": ["query"]
            }
        )
    ]
