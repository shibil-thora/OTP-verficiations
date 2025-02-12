import requests
from auth import gupshup_api_key

url = "https://api.gupshup.io/wa/api/v1/msg"

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
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded", 
    "apikey": gupshup_api_key
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)