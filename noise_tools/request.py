# https://github.com/xxxbrian/mcp-rquest
from mcp import types
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        types.Tool(
            name="http_get",
            description="Make an HTTP GET request to the specified URL",
            inputSchema={
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {"type": "string", "description": "URL to send the request to"},
                    "proxy": {"type": "string", "description": "Proxy to use for the request"},
                    "headers": {"type": "object", "description": "Headers to include in the request"},
                    "cookies": {"type": "object", "description": "Cookies to include in the request"},
                    "allow_redirects": {"type": "boolean", "description": "Whether to follow redirects"},
                    "max_redirects": {"type": "integer", "description": "Maximum number of redirects to follow"},
                    "auth": {"type": "string", "description": "Authentication credentials"},
                    "bearer_auth": {"type": "string", "description": "Bearer token for authentication"},
                    "basic_auth": {"type": "array", "description": "Basic auth credentials as [username, password]"},
                    "query": {"type": "array", "description": "Query parameters as [[key, value], ...]"},
                    "force_store_response_content": {"type": "boolean",
                                                     "description": "Force storing response content regardless of size"},
                }
            }
        ),
        types.Tool(
            name="http_post",
            description="Make an HTTP POST request to the specified URL",
            inputSchema={
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {"type": "string", "description": "URL to send the request to"},
                    "proxy": {"type": "string", "description": "Proxy to use for the request"},
                    "headers": {"type": "object", "description": "Headers to include in the request"},
                    "cookies": {"type": "object", "description": "Cookies to include in the request"},
                    "allow_redirects": {"type": "boolean", "description": "Whether to follow redirects"},
                    "max_redirects": {"type": "integer", "description": "Maximum number of redirects to follow"},
                    "auth": {"type": "string", "description": "Authentication credentials"},
                    "bearer_auth": {"type": "string", "description": "Bearer token for authentication"},
                    "basic_auth": {"type": "array", "description": "Basic auth credentials as [username, password]"},
                    "query": {"type": "array", "description": "Query parameters as [[key, value], ...]"},
                    "form": {"type": "array", "description": "Form data as [[key, value], ...]"},
                    "json_payload": {"type": "object", "description": "JSON payload"},
                    "body": {"type": "object", "description": "Request body"},
                    "multipart": {"type": "array", "description": "Multipart data as [[key, value], ...]"},
                    "force_store_response_content": {"type": "boolean",
                                                     "description": "Force storing response content regardless of size"},
                }
            }
        ),
        types.Tool(
            name="http_put",
            description="Make an HTTP PUT request to the specified URL",
            inputSchema={
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {"type": "string", "description": "URL to send the request to"},
                    "proxy": {"type": "string", "description": "Proxy to use for the request"},
                    "headers": {"type": "object", "description": "Headers to include in the request"},
                    "cookies": {"type": "object", "description": "Cookies to include in the request"},
                    "allow_redirects": {"type": "boolean", "description": "Whether to follow redirects"},
                    "max_redirects": {"type": "integer", "description": "Maximum number of redirects to follow"},
                    "auth": {"type": "string", "description": "Authentication credentials"},
                    "bearer_auth": {"type": "string", "description": "Bearer token for authentication"},
                    "basic_auth": {"type": "array", "description": "Basic auth credentials as [username, password]"},
                    "query": {"type": "array", "description": "Query parameters as [[key, value], ...]"},
                    "form": {"type": "array", "description": "Form data as [[key, value], ...]"},
                    "json_payload": {"type": "object", "description": "JSON payload"},
                    "body": {"type": "object", "description": "Request body"},
                    "multipart": {"type": "array", "description": "Multipart data as [[key, value], ...]"},
                    "force_store_response_content": {"type": "boolean",
                                                     "description": "Force storing response content regardless of size"},
                }
            }
        ),
        types.Tool(
            name="http_delete",
            description="Make an HTTP DELETE request to the specified URL",
            inputSchema={
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {"type": "string", "description": "URL to send the request to"},
                    "proxy": {"type": "string", "description": "Proxy to use for the request"},
                    "headers": {"type": "object", "description": "Headers to include in the request"},
                    "cookies": {"type": "object", "description": "Cookies to include in the request"},
                    "allow_redirects": {"type": "boolean", "description": "Whether to follow redirects"},
                    "max_redirects": {"type": "integer", "description": "Maximum number of redirects to follow"},
                    "auth": {"type": "string", "description": "Authentication credentials"},
                    "bearer_auth": {"type": "string", "description": "Bearer token for authentication"},
                    "basic_auth": {"type": "array", "description": "Basic auth credentials as [username, password]"},
                    "query": {"type": "array", "description": "Query parameters as [[key, value], ...]"},
                    "force_store_response_content": {"type": "boolean",
                                                     "description": "Force storing response content regardless of size"},
                }
            }
        ),
        types.Tool(
            name="http_patch",
            description="Make an HTTP PATCH request to the specified URL",
            inputSchema={
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {"type": "string", "description": "URL to send the request to"},
                    "proxy": {"type": "string", "description": "Proxy to use for the request"},
                    "headers": {"type": "object", "description": "Headers to include in the request"},
                    "cookies": {"type": "object", "description": "Cookies to include in the request"},
                    "allow_redirects": {"type": "boolean", "description": "Whether to follow redirects"},
                    "max_redirects": {"type": "integer", "description": "Maximum number of redirects to follow"},
                    "auth": {"type": "string", "description": "Authentication credentials"},
                    "bearer_auth": {"type": "string", "description": "Bearer token for authentication"},
                    "basic_auth": {"type": "array", "description": "Basic auth credentials as [username, password]"},
                    "query": {"type": "array", "description": "Query parameters as [[key, value], ...]"},
                    "form": {"type": "array", "description": "Form data as [[key, value], ...]"},
                    "json_payload": {"type": "object", "description": "JSON payload"},
                    "body": {"type": "object", "description": "Request body"},
                    "multipart": {"type": "array", "description": "Multipart data as [[key, value], ...]"},
                    "force_store_response_content": {"type": "boolean",
                                                     "description": "Force storing response content regardless of size"},
                }
            }
        ),
        types.Tool(
            name="http_head",
            description="Make an HTTP HEAD request to retrieve only headers from the specified URL",
            inputSchema={
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {"type": "string", "description": "URL to send the request to"},
                    "proxy": {"type": "string", "description": "Proxy to use for the request"},
                    "headers": {"type": "object", "description": "Headers to include in the request"},
                    "cookies": {"type": "object", "description": "Cookies to include in the request"},
                    "allow_redirects": {"type": "boolean", "description": "Whether to follow redirects"},
                    "max_redirects": {"type": "integer", "description": "Maximum number of redirects to follow"},
                    "auth": {"type": "string", "description": "Authentication credentials"},
                    "bearer_auth": {"type": "string", "description": "Bearer token for authentication"},
                    "basic_auth": {"type": "array", "description": "Basic auth credentials as [username, password]"},
                    "query": {"type": "array", "description": "Query parameters as [[key, value], ...]"},
                    "force_store_response_content": {"type": "boolean",
                                                     "description": "Force storing response content regardless of size"},
                }
            }
        ),
        types.Tool(
            name="http_options",
            description="Make an HTTP OPTIONS request to retrieve options for the specified URL",
            inputSchema={
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {"type": "string", "description": "URL to send the request to"},
                    "proxy": {"type": "string", "description": "Proxy to use for the request"},
                    "headers": {"type": "object", "description": "Headers to include in the request"},
                    "cookies": {"type": "object", "description": "Cookies to include in the request"},
                    "allow_redirects": {"type": "boolean", "description": "Whether to follow redirects"},
                    "max_redirects": {"type": "integer", "description": "Maximum number of redirects to follow"},
                    "auth": {"type": "string", "description": "Authentication credentials"},
                    "bearer_auth": {"type": "string", "description": "Bearer token for authentication"},
                    "basic_auth": {"type": "array", "description": "Basic auth credentials as [username, password]"},
                    "query": {"type": "array", "description": "Query parameters as [[key, value], ...]"},
                    "force_store_response_content": {"type": "boolean",
                                                     "description": "Force storing response content regardless of size"},
                }
            }
        ),
        types.Tool(
            name="http_trace",
            description="Make an HTTP TRACE request for diagnostic tracing of the specified URL",
            inputSchema={
                "type": "object",
                "required": ["url"],
                "properties": {
                    "url": {"type": "string", "description": "URL to send the request to"},
                    "proxy": {"type": "string", "description": "Proxy to use for the request"},
                    "headers": {"type": "object", "description": "Headers to include in the request"},
                    "cookies": {"type": "object", "description": "Cookies to include in the request"},
                    "allow_redirects": {"type": "boolean", "description": "Whether to follow redirects"},
                    "max_redirects": {"type": "integer", "description": "Maximum number of redirects to follow"},
                    "auth": {"type": "string", "description": "Authentication credentials"},
                    "bearer_auth": {"type": "string", "description": "Bearer token for authentication"},
                    "basic_auth": {"type": "array", "description": "Basic auth credentials as [username, password]"},
                    "query": {"type": "array", "description": "Query parameters as [[key, value], ...]"},
                    "force_store_response_content": {"type": "boolean",
                                                     "description": "Force storing response content regardless of size"},
                }
            }
        ),
        # HTTP Response tools
        types.Tool(
            name="get_stored_response",
            description="Retrieve a stored HTTP response by its ID",
            inputSchema={
                "type": "object",
                "required": ["response_id"],
                "properties": {
                    "response_id": {"type": "string", "description": "ID of the stored response"},
                    "start_line": {"type": "integer", "description": "Starting line number (1-indexed)"},
                    "end_line": {"type": "integer", "description": "Ending line number (inclusive)"},
                }
            }
        ),
        types.Tool(
            name="get_stored_response_with_markdown",
            description="Retrieve a stored HTTP response by its ID and convert it to Markdown format. Supports HTML and PDF content types. (Converting large PDF to Markdown may cause timeout, just wait and try again.)",
            inputSchema={
                "type": "object",
                "required": ["response_id"],
                "properties": {
                    "response_id": {"type": "string", "description": "ID of the stored response"},
                }
            }
        ),
        # PDF Model-related tools
        types.Tool(
            name="get_model_state",
            description="Get the current state of the PDF models(used by `get_stored_response_with_markdown`) loading process",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="restart_model_loading",
            description="Restart the PDF models(used by `get_stored_response_with_markdown`) loading process if it failed or got stuck",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
    ]
