# https://github.com/isaacwasserman/mcp-snowflake-server
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="list_tables",
            description="List all tables in the Snowflake database",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        Tool(
            name="describe_table",
            description="Get the schema information for a specific table",
            inputSchema={
                "type": "object",
                "properties": {"table_name": {"type": "string", "description": "Name of the table to describe"}},
                "required": ["table_name"],
            },
        ),
        Tool(
            name="read_query",
            description="Execute a SELECT query.",
            inputSchema={
                "type": "object",
                "properties": {"query": {"type": "string", "description": "SELECT SQL query to execute"}},
                "required": ["query"],
            },
        ),
        Tool(
            name="append_insight",
            description="Add a data insight to the memo",
            inputSchema={
                "type": "object",
                "properties": {"insight": {"type": "string", "description": "Data insight discovered from analysis"}},
                "required": ["insight"],
            },
        ),
        Tool(
            name="write_query",
            description="Execute an INSERT, UPDATE, or DELETE query on the Snowflake database",
            inputSchema={
                "type": "object",
                "properties": {"query": {"type": "string", "description": "SQL query to execute"}},
                "required": ["query"],
            },
        ),
        Tool(
            name="create_table",
            description="Create a new table in the Snowflake database",
            inputSchema={
                "type": "object",
                "properties": {"query": {"type": "string", "description": "CREATE TABLE SQL statement"}},
                "required": ["query"],
            },
        )
    ]
