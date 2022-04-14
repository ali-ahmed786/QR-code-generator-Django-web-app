from django.urls import path
from . import views
app_name = "passwordGenerator"
urlpatterns=[
    path("", views.index, name="passGenIndex"),
    path("generatePassword/", views.generatePassword, name="generatePassword")
]