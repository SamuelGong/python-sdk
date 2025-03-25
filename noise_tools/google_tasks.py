from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search",
            description="Search for a task in Google Tasks",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="list",
            description="List all tasks in Google Tasks",
            inputSchema={
                "type": "object",
                "properties": {
                    "cursor": {
                        "type": "string",
                        "description": "Cursor for pagination"
                    }
                }
            }
        ),
        Tool(
            name="create",
            description="Create a new task in Google Tasks",
            inputSchema={
                "type": "object",
                "properties": {
                    "taskListId": {
                        "type": "string",
                        "description": "Task list ID"
                    },
                    "title": {
                        "type": "string",
                        "description": "Task title"
                    },
                    "notes": {
                        "type": "string",
                        "description": "Task notes"
                    },
                    "due": {
                        "type": "string",
                        "description": "Due date"
                    }
                },
                "required": ["title"]
            }
        ),
        Tool(
            name="clear",
            description="Clear completed tasks from a Google Tasks task list",
            inputSchema={
                "type": "object",
                "properties": {
                    "taskListId": {
                        "type": "string",
                        "description": "Task list ID"
                    }
                },
                "required": ["taskListId"]
            }
        ),
        Tool(
            name="delete",
            description="Delete a task in Google Tasks",
            inputSchema={
                "type": "object",
                "properties": {
                    "taskListId": {
                        "type": "string",
                        "description": "Task list ID"
                    },
                    "id": {
                        "type": "string",
                        "description": "Task id"
                    }
                },
                "required": ["id", "taskListId"]
            }
        ),
        Tool(
            name="update",
            description="Update a task in Google Tasks",
            inputSchema={
                "type": "object",
                "properties": {
                    "taskListId": {
                        "type": "string",
                        "description": "Task list ID"
                    },
                    "id": {
                        "type": "string",
                        "description": "Task ID"
                    },
                    "uri": {
                        "type": "string",
                        "description": "Task URI"
                    },
                    "title": {
                        "type": "string",
                        "description": "Task title"
                    },
                    "notes": {
                        "type": "string",
                        "description": "Task notes"
                    },
                    "status": {
                        "type": "string",
                        "enum": ["needsAction", "completed"],
                        "description": "Task status (needsAction or completed)"
                    },
                    "due": {
                        "type": "string",
                        "description": "Due date"
                    }
                },
                "required": ["id", "uri"]
            }
        )
    ]
