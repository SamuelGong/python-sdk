# https://github.com/v-3/google-calendar
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="list_events",
            description="List calendar events within a specified time range",
            inputSchema={
                "type": "object",
                "properties": {
                    "timeMin": {
                        "type": "string",
                        "description": "Start time (ISO string)"
                    },
                    "timeMax": {
                        "type": "string",
                        "description": "End time (ISO string)"
                    },
                    "maxResults": {
                        "type": "number",
                        "description": "Maximum number of events to return"
                    }
                }
            }
        ),
        Tool(
            name="create_event",
            description="Create a new calendar event",
            inputSchema={
                "type": "object",
                "properties": {
                    "summary": {
                        "type": "string",
                        "description": "Event title"
                    },
                    "description": {
                        "type": "string",
                        "description": "Event description"
                    },
                    "startTime": {
                        "type": "string",
                        "description": "Event start time (ISO string)"
                    },
                    "endTime": {
                        "type": "string",
                        "description": "Event end time (ISO string)"
                    },
                    "attendees": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "List of attendee email addresses"
                    }
                },
                "required": ["summary", "startTime", "endTime"]
            }
        ),
        Tool(
            name="update_event",
            description="Update an existing calendar event",
            inputSchema={
                "type": "object",
                "properties": {
                    "eventId": {
                        "type": "string",
                        "description": "ID of the event to update"
                    },
                    "summary": {
                        "type": "string",
                        "description": "New event title"
                    },
                    "description": {
                        "type": "string",
                        "description": "New event description"
                    },
                    "startTime": {
                        "type": "string",
                        "description": "New start time (ISO string)"
                    },
                    "endTime": {
                        "type": "string",
                        "description": "New end time (ISO string)"
                    }
                },
                "required": ["eventId"]
            }
        ),
        Tool(
            name="delete_event",
            description="Delete a calendar event",
            inputSchema={
                "type": "object",
                "properties": {
                    "eventId": {
                        "type": "string",
                        "description": "ID of the event to delete"
                    }
                },
                "required": ["eventId"]
            }
        ),
        Tool(
            name="find_free_time",
            description="Find available time slots in the calendar",
            inputSchema={
                "type": "object",
                "properties": {
                    "timeMin": {
                        "type": "string",
                        "description": "Start of time range (ISO string)"
                    },
                    "timeMax": {
                        "type": "string",
                        "description": "End of time range (ISO string)"
                    },
                    "duration": {
                        "type": "number",
                        "description": "Desired duration in minutes"
                    }
                },
                "required": ["timeMin", "timeMax", "duration"]
            }
        )
    ]
