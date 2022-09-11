import config
from twilio.rest import Client
from flight_data import FlightData


AUTH_TOKEN = config.twilio_auth_token
ACCOUNT_SID = config.twilio_account_sid
TWILIO_PHONE_NUMBER = config.twilio_phone_num
MY_PHONE_NUMBER = config.my_phone_num


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_emails(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER,
        )
        print(message.sid)
