# https://github.com/v-3/notion-server
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_pages",
            description="Search through Notion pages",
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
            name="read_page",
            description="Read a regular page's content (not for databases - use retrieve_database for databases). Shows block IDs with their types (needed for block operations)",
            inputSchema={
                "type": "object",
                "properties": {
                    "pageId": {
                        "type": "string",
                        "description": "ID of the page to read"
                    }
                },
                "required": ["pageId"]
            }
        ),
        Tool(
            name="create_page",
            description="Create a new page or database item. For database items, include 'properties' matching database schema. For pages, use 'title' and 'content'",
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Page title (optional)"
                    },
                    "content": {
                        "type": "string",
                        "description": "Page content in markdown format (optional)"
                    },
                    "parentPageId": {
                        "type": "string",
                        "description": "ID of the parent page where this page will be created"
                    },
                    "properties": {
                        "type": "object",
                        "description": "Additional properties for database items (optional)"
                    }
                },
                "required": ["parentPageId"]
            }
        ),
        Tool(
            name="update_page",
            description="Update an existing Notion page",
            inputSchema={
                "type": "object",
                "properties": {
                    "pageId": {
                        "type": "string",
                        "description": "ID of the page to update"
                    },
                    "content": {
                        "type": "string",
                        "description": "New content to append"
                    },
                    "type": {
                        "type": "string",
                        "enum": ["paragraph", "task", "todo", "heading", "image"],
                        "description": "Type of content to append",
                        "optional": True
                    },
                    "mode": {
                        "type": "string",
                        "enum": ["replace", "append", "merge"],
                        "description": "Update mode: replace all content, append to existing, or merge",
                        "optional": True
                    },
                    "position": {
                        "type": "string",
                        "enum": ["start", "end"],
                        "description": "Position for merge mode: start or end",
                        "optional": True
                    }
                },
                "required": ["pageId", "content"]
            }
        ),
        Tool(
            name="retrieve_comments",
            description="Get all comments from a page",
            inputSchema={
                "type": "object",
                "properties": {
                    "pageId": {
                        "type": "string",
                        "description": "ID of the page"
                    },
                    "startCursor": {
                        "type": "string",
                        "description": "Pagination cursor"
                    },
                    "pageSize": {
                        "type": "number",
                        "description": "Number of comments to retrieve (max 100)"
                    }
                },
                "required": ["pageId"]
            }
        ),
        Tool(
            name="add_comment",
            description="Add a comment to a page",
            inputSchema={
                "type": "object",
                "properties": {
                    "pageId": {
                        "type": "string",
                        "description": "ID of the page to comment on"
                    },
                    "content": {
                        "type": "string",
                        "description": "Comment text"
                    }
                },
                "required": ["pageId", "content"]
            }
        ),
        Tool(
            name="create_database",
            description="Create a new database in a page",
            inputSchema={
                "type": "object",
                "properties": {
                    "parentPageId": {
                        "type": "string",
                        "description": "ID of the parent page"
                    },
                    "title": {
                        "type": "string",
                        "description": "Database title"
                    },
                    "properties": {
                        "type": "object",
                        "description": "Database schema properties"
                    }
                },
                "required": ["parentPageId", "title", "properties"]
            }
        ),
        Tool(
            name="query_database",
            description="Query a database",
            inputSchema={
                "type": "object",
                "properties": {
                    "databaseId": {
                        "type": "string",
                        "description": "ID of the database"
                    },
                    "filter": {
                        "type": "object",
                        "description": "Filter conditions"
                    },
                    "sort": {
                        "type": "object",
                        "description": "Sort conditions"
                    }
                },
                "required": ["databaseId"]
            }
        ),
        Tool(
            name="update_block",
            description="Update a block's content (must use same type as original block, use read_page first to get block IDs and types)",
            inputSchema={
                "type": "object",
                "properties": {
                    "blockId": {
                        "type": "string",
                        "description": "ID of the block to update"
                    },
                    "content": {
                        "type": "string",
                        "description": "New content for the block"
                    },
                    "type": {
                        "type": "string",
                        "enum": [
                            "paragraph",
                            "heading_1",
                            "heading_2",
                            "heading_3",
                            "bulleted_list_item",
                            "numbered_list_item"
                        ],
                        "description": "Type of block"
                    }
                },
                "required": ["blockId", "content"]
            }
        ),
        Tool(
            name="delete_block",
            description="Delete a specific block from a page",
            inputSchema={
                "type": "object",
                "properties": {
                    "blockId": {
                        "type": "string",
                        "description": "ID of the block to delete"
                    }
                },
                "required": ["blockId"]
            }
        ),
        Tool(
            name="update_database_item",
            description="Update a database item's properties (use query_database first to see required property structure)",
            inputSchema={
                "type": "object",
                "properties": {
                    "pageId": {
                        "type": "string",
                        "description": "ID of the database item (page) to update"
                    },
                    "properties": {
                        "type": "object",
                        "description": "Properties to update"
                    }
                },
                "required": ["pageId", "properties"]
            }
        ),
        Tool(
            name="retrieve_database",
            description="Retrieve a database's metadata",
            inputSchema={
                "type": "object",
                "properties": {
                    "databaseId": {
                        "type": "string",
                        "description": "ID of the database to retrieve"
                    }
                },
                "required": ["databaseId"]
            }
        ),
        Tool(
            name="update_database",
            description="Update a database's properties",
            inputSchema={
                "type": "object",
                "properties": {
                    "databaseId": {
                        "type": "string",
                        "description": "ID of the database to update"
                    },
                    "title": {
                        "type": "string",
                        "description": "New title for the database"
                    },
                    "description": {
                        "type": "string",
                        "description": "New description for the database"
                    },
                    "properties": {
                        "type": "object",
                        "description": "Properties schema to update"
                    }
                },
                "required": ["databaseId"]
            }
        )
    ]
