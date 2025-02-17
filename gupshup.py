import requests
from auth import gupshup_api_key

url = "http://homeassistant:8123/api/states"

api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI2MGE0YTkwNzQ0ZDI0MjU4ODc0M2E5NTcxNTUwMWI3NCIsImlhdCI6MTczOTQ0NTIxOCwiZXhwIjoyMDU0ODA1MjE4fQ.f0NbgsVAo5-WClrXsbJFbzX-A4qX-wiKfTq9YzQtk0Q'

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