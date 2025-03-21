import os
import httpx
import random
from openai import OpenAI
from useless_tools import use_less_tools


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

available_tools = useful_tools + use_less_tools
random.seed(4)
random.shuffle(available_tools)


model = "ep-20250212105505-5zlbx"
instruction = f"You have a list of tools: {available_tools}"
query = (f"Name a listed tool with which I can get the weather alerts in California, if any. "
         f"Please strictly format your answer as: FINAL_ANSWER: [tool_name]/None")
messages = [
    {"role": "system", "content": instruction},
    {"role": "user", "content": query}
]

if __name__ == "__main__":
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
    }
    completion = endpoint.chat.completions.create(**payload)
    print(completion.choices[0].message.content)
    # expected output: FINAL_ANSWER: get_alerts
