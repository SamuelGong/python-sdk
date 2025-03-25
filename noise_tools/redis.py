# https://github.com/modelcontextprotocol/servers/blob/main/src/redis
from mcp.types import (
    Tool,
)


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="set",
            description="Set a Redis key-value pair with optional expiration",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "Redis key",
                    },
                    "value": {
                        "type": "string",
                        "description": "Value to store",
                    },
                    "expireSeconds": {
                        "type": "number",
                        "description": "Optional expiration time in seconds",
                    },
                },
                "required": ["key", "value"],
            },
        ),
        Tool(
            name="get",
            description="Get value by key from Redis",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "description": "Redis key to retrieve",
                    },
                },
                "required": ["key"],
            },
        ),
        Tool(
            name="delete",
            description="Delete one or more keys from Redis",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {
                        "oneOf": [
                            {"type": "string"},
                            {"type": "array", "items": {"type": "string"}}
                        ],
                        "description": "Key or array of keys to delete",
                    },
                },
                "required": ["key"],
            },
        ),
        Tool(
            name="list",
            description="List Redis keys matching a pattern",
            inputSchema={
                "type": "object",
                "properties": {
                    "pattern": {
                        "type": "string",
                        "description": "Pattern to match keys (default: *)",
                    },
                },
            },
        )
    ]