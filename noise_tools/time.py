# https://github.com/modelcontextprotocol/servers/tree/main/src/time
from datetime import datetime
from enum import Enum

from zoneinfo import ZoneInfo
from mcp.types import Tool
from mcp.shared.exceptions import McpError

from pydantic import BaseModel


class TimeTools(str, Enum):
    GET_CURRENT_TIME = "get_current_time"
    CONVERT_TIME = "convert_time"


class TimeResult(BaseModel):
    timezone: str
    datetime: str
    is_dst: bool


class TimeConversionResult(BaseModel):
    source: TimeResult
    target: TimeResult
    time_difference: str


class TimeConversionInput(BaseModel):
    source_tz: str
    time: str
    target_tz_list: list[str]


def get_local_tz(local_tz_override: str | None = None) -> ZoneInfo:
    if local_tz_override:
        return ZoneInfo(local_tz_override)

    # Get local timezone from datetime.now()
    tzinfo = datetime.now().astimezone(tz=None).tzinfo
    if tzinfo is not None:
        return ZoneInfo(str(tzinfo))
    raise McpError("Could not determine local timezone - tzinfo is None")


def get_zoneinfo(timezone_name: str) -> ZoneInfo:
    try:
        return ZoneInfo(timezone_name)
    except Exception as e:
        raise McpError(f"Invalid timezone: {str(e)}")


def list_tools() -> list[Tool]:
    """List available time tools."""
    local_tz = str(get_local_tz("UTC"))
    return [
        Tool(
            name=TimeTools.GET_CURRENT_TIME.value,
            description="Get current time in a specific timezones",
            inputSchema={
                "type": "object",
                "properties": {
                    "timezone": {
                        "type": "string",
                        "description": f"IANA timezone name (e.g., 'America/New_York', 'Europe/London'). Use '{local_tz}' as local timezone if no timezone provided by the user.",
                    }
                },
                "required": ["timezone"],
            },
        ),
        Tool(
            name=TimeTools.CONVERT_TIME.value,
            description="Convert time between timezones",
            inputSchema={
                "type": "object",
                "properties": {
                    "source_timezone": {
                        "type": "string",
                        "description": f"Source IANA timezone name (e.g., 'America/New_York', 'Europe/London'). Use '{local_tz}' as local timezone if no source timezone provided by the user.",
                    },
                    "time": {
                        "type": "string",
                        "description": "Time to convert in 24-hour format (HH:MM)",
                    },
                    "target_timezone": {
                        "type": "string",
                        "description": f"Target IANA timezone name (e.g., 'Asia/Tokyo', 'America/San_Francisco'). Use '{local_tz}' as local timezone if no target timezone provided by the user.",
                    },
                },
                "required": ["source_timezone", "time", "target_timezone"],
            },
        ),
    ]
