# https://github.com/ferrislucas/iterm-mcp
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="write_to_terminal",
            description="Writes text to the active iTerm terminal - often used to run a command in the terminal",
            inputSchema={
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command to run or text to write to the terminal"
                    }
                },
                "required": ["command"]
            }
        ),
        Tool(
            name="read_terminal_output",
            description="Reads the output from the active iTerm terminal",
            inputSchema={
                "type": "object",
                "properties": {
                    "linesOfOutput": {
                        "type": "number",
                        "description": "The number of lines of output to read."
                    }
                },
                "required": ["linesOfOutput"]
            }
        ),
        Tool(
            name="send_control_character",
            description="Sends a control character to the active iTerm terminal (e.g., Control-C)",
            inputSchema={
                "type": "object",
                "properties": {
                    "letter": {
                        "type": "string",
                        "description": "The letter corresponding to the control character (e.g., 'C' for Control-C)"
                    }
                },
                "required": ["letter"]
            }
        )

    ]
