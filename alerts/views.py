from django.shortcuts import render

from alerts.tasks import send_sms


def index(request):
    send_sms.delay()
    name = "alerts"
    return render(request, "index.html", {"name": name})
