# https://github.com/burningion/video-editing-mcp
from mcp import types
from mcp.types import Tool


def list_tools() -> list[Tool]:
    return [
        types.Tool(
            name="add-video",
            description="Upload video from URL",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "url": {"type": "string"},
                },
                "required": ["name", "url"],
            },
        ),
        types.Tool(
            name="search-remote-videos",
            description="Search remote videos hosted on Video Jungle by query",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Text search query"},
                    "limit": {
                        "type": "integer",
                        "default": 10,
                        "minimum": 1,
                        "description": "Maximum number of results to return",
                    },
                    "project_id": {
                        "type": "string",
                        "format": "uuid",
                        "description": "Project ID to scope the search",
                    },
                    "duration_min": {
                        "type": "number",
                        "minimum": 0,
                        "description": "Minimum video duration in seconds",
                    },
                    "duration_max": {
                        "type": "number",
                        "minimum": 0,
                        "description": "Maximum video duration in seconds",
                    },
                },
                "created_after": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Filter videos created after this datetime",
                },
                "created_before": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Filter videos created before this datetime",
                },
                "tags": {
                    "type": "array",
                    "items": {"type": "string"},
                    "uniqueItems": True,
                    "description": "Set of tags to filter by",
                },
                "include_segments": {
                    "type": "boolean",
                    "default": True,
                    "description": "Whether to include video segments in results",
                },
                "include_related": {
                    "type": "boolean",
                    "default": False,
                    "description": "Whether to include related videos",
                },
                "query_audio": {
                    "type": "string",
                    "description": "Audio search query",
                },
                "query_img": {
                    "type": "string",
                    "description": "Image search query",
                },
                "oneOf": [
                    {"required": ["query"]},
                ],
            },
        ),
        types.Tool(
            name="search-local-videos",
            description="Search local videos in Photos app by keyword",
            inputSchema={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string"},
                    "start_date": {
                        "type": "string",
                        "description": "ISO 8601 formatted datetime string (e.g. 2024-01-21T15:30:00Z)",
                    },
                    "end_date": {
                        "type": "string",
                        "description": "ISO 8601 formatted datetime string (e.g. 2024-01-21T15:30:00Z)",
                    },
                },
                "required": ["keyword"],
            },
        ),
        types.Tool(
            name="generate-edit-from-videos",
            description="Generate an edit from videos",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_id": {"type": "string", "description": "Project ID"},
                    "name": {"type": "string", "description": "Video Edit name"},
                    "resolution": {
                        "type": "string",
                        "description": "Video resolution. Examples include '1080p', '720p'",
                    },
                    "edit": {
                        "type": "array",
                        "cuts": {
                            "video_id": {"type": "string", "description": "Video UUID"},
                            "video_start_time": {
                                "type": "string",
                                "description": "Clip start time in 00:00:00.000 format",
                            },
                            "video_end_time": {
                                "type": "string",
                                "description": "Clip end time in 00:00:00.000 format",
                            },
                        },
                    },
                },
                "required": ["edit", "cuts", "name", "project_id"],
            },
        ),
        types.Tool(
            name="generate-edit-from-single-video",
            description="Generate a video edit from a single video",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_id": {"type": "string"},
                    "resolution": {"type": "string"},
                    "video_id": {"type": "string"},
                    "edit": {
                        "type": "array",
                        "cuts": {
                            "video_start_time": "time",
                            "video_end_time": "time",
                        },
                    },
                },
                "required": ["edit", "project_id", "video_id", "cuts"],
            },
        ),
        types.Tool(
            name="create-video-bar-chart-from-two-axis-data",
            description="Create a video bar chart from two-axis data",
            inputSchema={
                "type": "object",
                "properties": {
                    "x_values": {"type": "array", "items": {"type": "string"}},
                    "y_values": {"type": "array", "items": {"type": "number"}},
                    "x_label": {"type": "string"},
                    "y_label": {"type": "string"},
                    "title": {"type": "string"},
                    "filename": {"type": "string"},
                },
                "required": ["x_values", "y_values", "x_label", "y_label", "title"],
            },
        ),
        types.Tool(
            name="create-video-line-chart-from-two-axis-data",
            description="Create a video line chart from two-axis data",
            inputSchema={
                "type": "object",
                "properties": {
                    "x_values": {"type": "array", "items": {"type": "string"}},
                    "y_values": {"type": "array", "items": {"type": "number"}},
                    "x_label": {"type": "string"},
                    "y_label": {"type": "string"},
                    "title": {"type": "string"},
                    "filename": {"type": "string"},
                },
                "required": ["x_values", "y_values", "x_label", "y_label", "title"],
            },
        ),
    ]
