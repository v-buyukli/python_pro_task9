from celery import shared_task


@shared_task
def send_sms():
    print("Hello from celery process")
    print("send sms")
    print("End...")
