import smtplib

import config
from twilio.rest import Client


AUTH_TOKEN = config.twilio_auth_token
ACCOUNT_SID = config.twilio_account_sid
TWILIO_PHONE_NUMBER = config.twilio_phone_num
MY_PHONE_NUMBER = config.my_phone_num
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = config.my_email
MY_PASSWORD = config.my_password


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

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
