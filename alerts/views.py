from django.shortcuts import render


def index(request):
    name = "alerts"
    return render(request, "index.html", {"name": name})
