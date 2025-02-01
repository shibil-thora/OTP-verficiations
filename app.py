from twilio.rest import Client 
from auth import auth_token, account_sid

# Your Account SID and Auth Token from console.twilio.com
account_sid =  account_sid
auth_token  = auth_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+916238748856",
    from_="+18454488647",
    body="Hello from Python!")

print(message.sid)