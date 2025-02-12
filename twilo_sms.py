import os
from twilio.rest import Client
from dotenv import load_dotenv 
load_dotenv()

 
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="asdfasdfasfasdfsjfl;kakjs f;lkasj;flkasj ;foiuwpeevuopwpiufsaoidufmpovisadjfd;asjdvfjaowiejpvaoijfvvsajdfvoiajwjperrijvapfjvaskdfj;lasjdvf",
    from_="+19289107262",
    to="+916238748856",
)

print(message.body)