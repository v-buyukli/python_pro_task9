from celery import shared_task
from twilio.rest import Client


@shared_task
def send_sms(number, account_sid, auth_token):
    print("Start task...")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hello from Twilio",
        from_="+12706122090",
        to=number
    )
    print(f"status = {message.status}, sid = {message.sid}")
