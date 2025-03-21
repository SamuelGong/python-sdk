import os
import httpx
from openai import OpenAI


useful_tools = [
    {
        'type': 'function',
        'function': {
            'name': 'get_alerts',
            'description': 'Get weather alerts for a US state.\n\n    Args:\n        state: Two-letter US state code (e.g. CA, NY)\n    ',
            'input_schema': {
                'properties': {
                    'state': {
                        'title': 'State',
                        'type': 'string'
                    }
                },
                'required': ['state'],
                'title': 'get_alertsArguments',
                'type': 'object'
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'get_forecast',
            'description': 'Get weather forecast for a location.\n\n    Args:\n        latitude: Latitude of the location\n        longitude: Longitude of the location\n    ',
            'input_schema': {
                'properties': {
                    'latitude': {
                        'title': 'Latitude',
                        'type': 'number'
                    },
                    'longitude': {
                        'title': 'Longitude',
                        'type': 'number'
                    }
                },
                'required': ['latitude', 'longitude'],
                'title': 'get_forecastArguments',
                'type': 'object'
            }
        }
    }
]

available_tools = useful_tools + []

model = "ep-20250212105505-5zlbx"
query = "What are the weather alerts in California?"
messages = [
    {
        "role": "user",
        "content": query
    }
]
endpoint = OpenAI(
    api_key=os.getenv("ARK_API_KEY"),
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    http_client=httpx.Client(
        verify=False  # important for company use
    )
)
payload = {
    "model": model,
    "messages": messages,
    "tools": available_tools
}
completion = endpoint.chat.completions.create(**payload)
print(completion.choices[0].message.tool_calls)
