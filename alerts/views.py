from django.shortcuts import render
from django.conf import settings

from alerts.forms import PhoneForm
from alerts.tasks import send_sms


def index(request):
    text = "Hello"
    return render(request, "index.html", {"text": text})


def phone_number(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data["phone"]
            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            send_sms.delay(number, account_sid, auth_token)
            text = f"Sending a message to a phone number: {number}"
            return render(request, "index.html", {"text": text})
    else:
        form = PhoneForm()
    return render(request, "phone_number.html", {"form": form})
