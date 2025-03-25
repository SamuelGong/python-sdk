# https://github.com/suhail-ak-s/mcp-typesense-server
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="typesense_query",
            description="Search for relevant documents in the TypeSense database based on the user's query.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query entered by the user."
                    },
                    "collection": {
                        "type": "string",
                        "description": "The name of the TypeSense collection to search within."
                    },
                    "query_by": {
                        "type": "string",
                        "description": "Comma-separated fields to search in the collection, e.g., 'title,content'."
                    },
                    "filter_by": {
                        "type": "string",
                        "description": "Optional filtering criteria, e.g., 'category:Chatbot'."
                    },
                    "sort_by": {
                        "type": "string",
                        "description": "Sorting criteria, e.g., 'created_at:desc'."
                    },
                    "limit": {
                        "type": "integer",
                        "description": "The maximum number of results to return.",
                        "default": 10
                    }
                },
                "required": ["query", "collection", "query_by"]
            }
        ),
        Tool(
            name="typesense_get_document",
            description="Retrieve a specific document by ID from a Typesense collection",
            inputSchema={
                "type": "object",
                "properties": {
                    "collection": {
                        "type": "string",
                        "description": "The name of the TypeSense collection"
                    },
                    "document_id": {
                        "type": "string",
                        "description": "The ID of the document to retrieve"
                    }
                },
                "required": ["collection", "document_id"]
            }
        ),
        Tool(
            name="typesense_collection_stats",
            description="Get statistics about a Typesense collection",
            inputSchema={
                "type": "object",
                "properties": {
                    "collection": {
                        "type": "string",
                        "description": "The name of the TypeSense collection"
                    }
                },
                "required": ["collection"]
            }
        )
    ]
