import requests
from auth import fast2sms_api_key

url = "https://www.fast2sms.com/dev/bulkV2"

payload = "sender_id=ONWRDS&message=180227&variables_values=133345|asdaswdx&route=dlt&numbers=6238748856"
headers = {
    'authorization': fast2sms_api_key,
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)