from django.urls import path
from . import views
app_name = "qrCode"
urlpatterns=[
    path("", views.index, name="index"),
    path("qrcode",views.generateQR,name="generateQR"),
]