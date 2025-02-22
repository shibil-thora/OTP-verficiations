import requests
from auth import gupshup_api_key

url = "http://homeassistant:8123/api/states"

api_key = gupshup_api_key

payload = { 
    "message":
    { 
        "text":"Welcome to Gupshup",
        "type": "text", 
        "previewUrl":False
    }, 
    "source": "916238748856", 
    "destination": "919072200430", 
    "src": {
        "name": "myapp"
    }
}

headers = {
    "content-type": "application/json", 
    "Authorization": f'Bearer {api_key}'
}

response = requests.get(url, headers=headers)

print(response.json())
