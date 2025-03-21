# https://github.com/vidhupv/x-mcp/blob/main/src/x_mcp/server.py
from mcp.types import Tool


def list_tools() -> list[Tool]:
    """List available tools for interacting with Twitter/X."""
    return [
        Tool(
            name="create_draft_tweet",
            description="Create a draft tweet",
            inputSchema={
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "The content of the tweet",
                    },
                },
                "required": ["content"],
            },
        ),
        Tool(
            name="create_draft_thread",
            description="Create a draft tweet thread",
            inputSchema={
                "type": "object",
                "properties": {
                    "contents": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "An array of tweet contents for the thread",
                    },
                },
                "required": ["contents"],
            },
        ),
        Tool(
            name="list_drafts",
            description="List all draft tweets and threads",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        Tool(
            name="publish_draft",
            description="Publish a draft tweet or thread",
            inputSchema={
                "type": "object",
                "properties": {
                    "draft_id": {
                        "type": "string",
                        "description": "ID of the draft to publish",
                    },
                },
                "required": ["draft_id"],
            },
        ),
        Tool(
            name="delete_draft",
            description="Delete a draft tweet or thread",
            inputSchema={
                "type": "object",
                "properties": {
                    "draft_id": {
                        "type": "string",
                        "description": "ID of the draft to delete",
                    },
                },
                "required": ["draft_id"],
            },
        ),
    ]
