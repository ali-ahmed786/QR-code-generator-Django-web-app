from django.urls import path
from . import views
app_name = "regextool"
urlpatterns=[
    path("", views.index, name="regIndex"),
    path("regexcheck", views.regCheck, name="regCheck")
]
