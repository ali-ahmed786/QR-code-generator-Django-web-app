from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="regIndex"),
    path("regexcheck", views.regCheck, name="regCheck")
]
