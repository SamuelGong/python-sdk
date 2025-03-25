# https://github.com/SimonB97/win-cli-mcp-server
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="execute_command",
            description="""Execute a command in the specified shell (powershell, cmd, or gitbash)

Example usage (PowerShell):
\`\`\`json
{
  "shell": "powershell",
  "command": "Get-Process | Select-Object -First 5",
  "workingDir": "C:\\Users\\username"
}
\`\`\`

Example usage (CMD):
\`\`\`json
{
  "shell": "cmd",
  "command": "dir /b",
  "workingDir": "C:\\Projects"
}
\`\`\`

Example usage (Git Bash):
\`\`\`json
{
  "shell": "gitbash",
  "command": "ls -la",
  "workingDir": "/c/Users/username"
}
\`\`\`""",
            inputSchema={
                "type": "object",
                "properties": {
                    "shell": {
                        "type": "string",
                        "enum": [],  # simplify by Zhifeng Jiang
                        "description": "Shell to use for command execution"
                    },
                    "command": {
                        "type": "string",
                        "description": "Command to execute"
                    },
                    "workingDir": {
                        "type": "string",
                        "description": "Working directory for command execution (optional)"
                    }
                },
                "required": ["shell", "command"]
            }
        ),
        Tool(
            name="get_command_history",
            description="""Get the history of executed commands

Example usage:
\`\`\`json
{
  "limit": 5
}
\`\`\`

Example response:
\`\`\`json
[
  {
    "command": "Get-Process",
    "output": "...",
    "timestamp": "2024-03-20T10:30:00Z",
    "exitCode": 0
  }
]
\`\`\`""",
            inputSchema={
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of history entries to return (default: 10, max: ${this.config.security.maxHistorySize})"
                    }
                }
            }
        ),
        Tool(
            name="ssh_execute",
            description="""Execute a command on a remote host via SSH

Example usage:
\`\`\`json
{
  "connectionId": "raspberry-pi",
  "command": "uname -a"
}
\`\`\`

Configuration required in config.json:
\`\`\`json
{
  "ssh": {
    "enabled": true,
    "connections": {
      "raspberry-pi": {
        "host": "raspberrypi.local",
        "port": 22,
        "username": "pi",
        "password": "raspberry"
      }
    }
  }
}
\`\`\`""",
            inputSchema={
                "type": "object",
                "properties": {
                    "connectionId": {
                        "type": "string",
                        "description": "ID of the SSH connection to use",
                        "enum": []  # Simplifies by Zhifeng Jiang
                    },
                    "command": {
                        "type": "string",
                        "description": "Command to execute"
                    }
                },
                "required": ["connectionId", "command"]
            }
        ),
        Tool(
            name="ssh_disconnect",
            description="""Disconnect from an SSH server

Example usage:
\`\`\`json
{
  "connectionId": "raspberry-pi"
}
\`\`\`

Use this to cleanly close SSH connections when they're no longer needed.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "connectionId": {
                        "type": "string",
                        "description": "ID of the SSH connection to disconnect",
                        "enum": []  # Simplified by Zhifeng Jiang
                    }
                },
                "required": ["connectionId"]
            }
        ),
        Tool(
            name="create_ssh_connection",
            description="Create a new SSH connection",
            inputSchema={
                "type": "object",
                "properties": {
                    "connectionId": {
                        "type": "string",
                        "description": "ID of the SSH connection"
                    },
                    "connectionConfig": {
                        "type": "object",
                        "properties": {
                            "host": {
                                "type": "string",
                                "description": "Host of the SSH connection"
                            },
                            "port": {
                                "type": "number",
                                "description": "Port of the SSH connection"
                            },
                            "username": {
                                "type": "string",
                                "description": "Username for the SSH connection"
                            },
                            "password": {
                                "type": "string",
                                "description": "Password for the SSH connection"
                            },
                            "privateKeyPath": {
                                "type": "string",
                                "description": "Path to the private key for the SSH connection"
                            }
                        },
                        "required": ["connectionId", "connectionConfig"]
                    }
                }
            }
        ),
        Tool(
            name="read_ssh_connections",
            description="Read all SSH connections",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="update_ssh_connection",
            description="Update an existing SSH connection",
            inputSchema={
                "type": "object",
                "properties": {
                    "connectionId": {
                        "type": "string",
                        "description": "ID of the SSH connection to update"
                    },
                    "connectionConfig": {
                        "type": "object",
                        "properties": {
                            "host": {
                                "type": "string",
                                "description": "Host of the SSH connection"
                            },
                            "port": {
                                "type": "number",
                                "description": "Port of the SSH connection"
                            },
                            "username": {
                                "type": "string",
                                "description": "Username for the SSH connection"
                            },
                            "password": {
                                "type": "string",
                                "description": "Password for the SSH connection"
                            },
                            "privateKeyPath": {
                                "type": "string",
                                "description": "Path to the private key for the SSH connection"
                            }
                        },
                        "required": ["connectionId", "connectionConfig"]
                    }
                }
            }
        ),
        Tool(
            name="delete_ssh_connection",
            description="Delete an existing SSH connection",
            inputSchema={
                "type": "object",
                "properties": {
                    "connectionId": {
                        "type": "string",
                        "description": "ID of the SSH connection to delete"
                    }
                },
                "required": ["connectionId"]
            }
        ),
        Tool(
            name="get_current_directory",
            description="Get the current working directory",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]