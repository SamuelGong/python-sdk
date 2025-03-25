# https://github.com/executeautomation/mcp-playwright
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="playwright_navigate",
            description="Navigate to a URL",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL to navigate to the website specified"
                    },
                    "browserType": {
                        "type": "string",
                        "description": "Browser type to use (chromium, firefox, webkit). Defaults to chromium",
                        "enum": ["chromium", "firefox", "webkit"]
                    },
                    "width": {
                        "type": "number",
                        "description": "Viewport width in pixels (default: 1280)"
                    },
                    "height": {
                        "type": "number",
                        "description": "Viewport height in pixels (default: 720)"
                    },
                    "timeout": {
                        "type": "number",
                        "description": "Navigation timeout in milliseconds"
                    },
                    "waitUntil": {
                        "type": "string",
                        "description": "Navigation wait condition"
                    },
                    "headless": {
                        "type": "boolean",
                        "description": "Run browser in headless mode (default: false)"
                    }
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="playwright_screenshot",
            description="Take a screenshot of the current page or a specific element",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name for the screenshot"
                    },
                    "selector": {
                        "type": "string",
                        "description": "CSS selector for element to screenshot"
                    },
                    "width": {
                        "type": "number",
                        "description": "Width in pixels (default: 800)"
                    },
                    "height": {
                        "type": "number",
                        "description": "Height in pixels (default: 600)"
                    },
                    "storeBase64": {
                        "type": "boolean",
                        "description": "Store screenshot in base64 format (default: true)"
                    },
                    "fullPage": {
                        "type": "boolean",
                        "description": "Store screenshot of the entire page (default: false)"
                    },
                    "savePng": {
                        "type": "boolean",
                        "description": "Save screenshot as PNG file (default: false)"
                    },
                    "downloadsDir": {
                        "type": "string",
                        "description": "Custom downloads directory path (default: user's Downloads folder)"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="playwright_click",
            description="Click an element on the page",
            inputSchema={
                "type": "object",
                "properties": {
                    "selector": {
                        "type": "string",
                        "description": "CSS selector for the element to click"
                    }
                },
                "required": ["selector"]
            }
        ),
        Tool(
            name="playwright_iframe_click",
            description="Click an element in an iframe on the page",
            inputSchema={
                "type": "object",
                "properties": {
                    "iframeSelector": {
                        "type": "string",
                        "description": "CSS selector for the iframe containing the element to click"
                    },
                    "selector": {
                        "type": "string",
                        "description": "CSS selector for the element to click"
                    }
                },
                "required": ["iframeSelector", "selector"]
            }
        ),
        Tool(
            name="playwright_fill",
            description="fill out an input field",
            inputSchema={
                "type": "object",
                "properties": {
                    "selector": {
                        "type": "string",
                        "description": "CSS selector for input field"
                    },
                    "value": {
                        "type": "string",
                        "description": "Value to fill"
                    }
                },
                "required": ["selector", "value"]
            }
        ),
        Tool(
            name="playwright_select",
            description="Select an element on the page with Select tag",
            inputSchema={
                "type": "object",
                "properties": {
                    "selector": {
                        "type": "string",
                        "description": "CSS selector for element to select"
                    },
                    "value": {
                        "type": "string",
                        "description": "Value to select"
                    }
                },
                "required": ["selector", "value"]
            }
        ),
        Tool(
            name="playwright_hover",
            description="Hover an element on the page",
            inputSchema={
                "type": "object",
                "properties": {
                    "selector": {
                        "type": "string",
                        "description": "CSS selector for element to hover"
                    }
                },
                "required": ["selector"]
            }
        ),
        Tool(
            name="playwright_evaluate",
            description="Execute JavaScript in the browser console",
            inputSchema={
                "type": "object",
                "properties": {
                    "script": {
                        "type": "string",
                        "description": "JavaScript code to execute"
                    }
                },
                "required": ["script"]
            }
        ),
        Tool(
            name="playwright_console_logs",
            description="Retrieve console logs from the browser with filtering options",
            inputSchema={
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "description": "Type of logs to retrieve (all, error, warning, log, info, debug)",
                        "enum": ["all", "error", "warning", "log", "info", "debug"]
                    },
                    "search": {
                        "type": "string",
                        "description": "Text to search for in logs (handles text with square brackets)"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of logs to return"
                    },
                    "clear": {
                        "type": "boolean",
                        "description": "Whether to clear logs after retrieval (default: false)"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="playwright_close",
            description="Close the browser and release all resources",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="playwright_get",
            description="Perform an HTTP GET request",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL to perform GET operation"
                    }
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="playwright_post",
            description="Perform an HTTP POST request",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL to perform POST operation"
                    },
                    "value": {
                        "type": "string",
                        "description": "Data to post in the body"
                    },
                    "token": {
                        "type": "string",
                        "description": "Bearer token for authorization"
                    },
                    "headers": {
                        "type": "object",
                        "description": "Additional headers to include in the request",
                        "additionalProperties": {"type": "string"}
                    }
                },
                "required": ["url", "value"]
            }
        ),
        Tool(
            name="playwright_put",
            description="Perform an HTTP PUT request",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL to perform PUT operation"
                    },
                    "value": {
                        "type": "string",
                        "description": "Data to PUT in the body"
                    }
                },
                "required": ["url", "value"]
            }
        ),
        Tool(
            name="playwright_patch",
            description="Perform an HTTP PATCH request",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL to perform PUT operation"
                    },
                    "value": {
                        "type": "string",
                        "description": "Data to PATCH in the body"
                    }
                },
                "required": ["url", "value"]
            }
        ),
        Tool(
            name="playwright_delete",
            description="Perform an HTTP DELETE request",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "URL to perform DELETE operation"
                    }
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="playwright_expect_response",
            description="Ask Playwright to start waiting for a HTTP response. This tool initiates the wait operation but does not wait for its completion.",
            inputSchema={
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "Unique & arbitrary identifier to be used for retrieving this response later with `Playwright_assert_response`."
                    },
                    "url": {
                        "type": "string",
                        "description": "URL pattern to match in the response."
                    }
                },
                "required": ["id", "url"]
            }
        ),
        Tool(
            name="playwright_assert_response",
            description="Wait for and validate a previously initiated HTTP response wait operation.",
            inputSchema={
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "description": "Identifier of the HTTP response initially expected using `Playwright_expect_response`."
                    },
                    "value": {
                        "type": "string",
                        "description": "Data to expect in the body of the HTTP response. If provided, the assertion will fail if this value is not found in the response body."
                    }
                },
                "required": ["id"]
            }
        ),
        Tool(
            name="playwright_custom_user_agent",
            description="Set a custom User Agent for the browser",
            inputSchema={
                "type": "object",
                "properties": {
                    "userAgent": {
                        "type": "string",
                        "description": "Custom User Agent for the Playwright browser instance"
                    }
                },
                "required": ["userAgent"]
            }
        )
    ]