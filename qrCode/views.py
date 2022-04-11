from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import qrcode


def index(request):
    return render(request, "qrCode/index.html")
def generateQR(request):
    url= request.POST.get('urlInput')
    name=request.POST.get('nameInput')
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    path='qrCode/static/qrCode/'+name+'.png'
    shortPath='qrCode/'+name+'.png'
    img.save(path)
    return render(request, "qrCode/qrcode.html", {
         "path": shortPath,
         "url": url
    })