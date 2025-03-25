# https://github.com/modelcontextprotocol/servers/blob/main/src/google-maps
from mcp.types import (
    Tool,
)


def list_tools() -> list[Tool]:
    return [
        Tool(
            name="maps_geocode",
            description="Convert an address into geographic coordinates",
            inputSchema={
                "type": "object",
                "properties": {
                    "address": {
                        "type": "string",
                        "description": "The address to geocode"
                    }
                },
                "required": ["address"]
            }
        ),
        Tool(
            name="maps_reverse_geocode",
            description="Convert coordinates into an address",
            inputSchema={
                "type": "object",
                "properties": {
                    "latitude": {
                        "type": "number",
                        "description": "Latitude coordinate"
                    },
                    "longitude": {
                        "type": "number",
                        "description": "Longitude coordinate"
                    }
                },
                "required": ["latitude", "longitude"]
            }
        ),
        Tool(
            name="maps_search_places",
            description="Search for places using Google Places API",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    },
                    "location": {
                        "type": "object",
                        "properties": {
                            "latitude": {"type": "number"},
                            "longitude": {"type": "number"}
                        },
                        "description": "Optional center point for the search"
                    },
                    "radius": {
                        "type": "number",
                        "description": "Search radius in meters (max 50000)"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="maps_place_details",
            description="Get detailed information about a specific place",
            inputSchema={
                "type": "object",
                "properties": {
                    "place_id": {
                        "type": "string",
                        "description": "The place ID to get details for"
                    }
                },
                "required": ["place_id"]
            }
        ),
        Tool(
            name="maps_distance_matrix",
            description="Calculate travel distance and time for multiple origins and destinations",
            inputSchema={
                "type": "object",
                "properties": {
                    "origins": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Array of origin addresses or coordinates"
                    },
                    "destinations": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Array of destination addresses or coordinates"
                    },
                    "mode": {
                        "type": "string",
                        "description": "Travel mode (driving, walking, bicycling, transit)",
                        "enum": ["driving", "walking", "bicycling", "transit"]
                    }
                },
                "required": ["origins", "destinations"]
            }
        ),
        Tool(
            name="maps_elevation",
            description="Get elevation data for locations on the earth",
            inputSchema={
                "type": "object",
                "properties": {
                    "locations": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "latitude": {"type": "number"},
                                "longitude": {"type": "number"}
                            },
                            "required": ["latitude", "longitude"]
                        },
                        "description": "Array of locations to get elevation for"
                    }
                },
                "required": ["locations"]
            }
        ),
        Tool(
            name="maps_directions",
            description="Get directions between two points",
            inputSchema={
                "type": "object",
                "properties": {
                    "origin": {
                        "type": "string",
                        'description': "Starting point address or coordinates"
                    },
                    "destination": {
                        "type": "string",
                        "description": "Ending point address or coordinates"
                    },
                    "mode": {
                        "type": "string",
                        "description": "Travel mode (driving, walking, bicycling, transit)",
                        "enum": ["driving", "walking", "bicycling", "transit"]
                    }
                },
                "required": ["origin", "destination"]
            }
        )
    ]