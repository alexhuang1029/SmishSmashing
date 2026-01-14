import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello. Testing 123 123 123!~@($)#$()",
                    from_='+18552168577',
                    to=''
                )
print("HI")
print(message.sid)
print("hello")
