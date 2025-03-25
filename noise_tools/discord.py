# https://github.com/v-3/discordmcp
from mcp.types import (
    Tool,
)


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="send-message",
            description="Send a message to a Discord channel",
            inputSchema={
                "type": "object",
                "properties": {
                    "server": {
                        "type": "string",
                        "description": 'Server name or ID (optional if bot is only in one server)',
                    },
                    "channel": {
                        "type": "string",
                        "description": 'Channel name (e.g., "general") or ID',
                    },
                    "message": {
                        "type": "string",
                        "description": "Message content to send",
                    },
                },
                "required": ["channel", "message"],
            },
        ),
        Tool(
            name="read-messages",
            description="Read recent messages from a Discord channel",
            inputSchema={
                "type": "object",
                "properties": {
                    "server": {
                        "type": "string",
                        "description": 'Server name or ID (optional if bot is only in one server)',
                    },
                    "channel": {
                        "type": "string",
                        "description": 'Channel name (e.g., "general") or ID',
                    },
                    "limit": {
                        "type": "number",
                        "description": "Number of messages to fetch (max 100)",
                        "default": 50,
                    },
                },
                "required": ["channel"],
            },
        )
    ]