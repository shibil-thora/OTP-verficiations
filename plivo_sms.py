from dotenv import load_dotenv 
load_dotenv() 
import requests

import plivo
from auth import plivo_auth_id, plivo_auth_token 

def outbound_sms(): 
    

    client = plivo.RestClient(plivo_auth_id, plivo_auth_token)
    response = client.messages.create(
        src='ONW8KVNK',
        dst='+917867894424',
        text='your otp is 123456',
       
        )
    print(response)
    #prints only the message_uuid
    print(response.message_uuid)

  
 
if __name__ == '__main__': 
    outbound_sms()