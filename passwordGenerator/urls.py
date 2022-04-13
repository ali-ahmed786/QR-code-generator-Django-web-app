from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name="passGenIndex"),
    path("generatePassword/", views.generatePassword, name="generatePassword")
]