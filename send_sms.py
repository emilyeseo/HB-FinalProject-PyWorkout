import os
import re
from twilio.rest import Client


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

# my_msg = "test test test"


if __name__ == '__main__':
    message = client.messages \
        .create(
            body='success',
            from_='+12143937243',
            to='+12146095612'
        )
