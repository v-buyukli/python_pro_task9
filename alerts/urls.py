from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("phone_number/", views.phone_number, name="phone_number"),
]
