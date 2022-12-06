from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners


# Create your views here.
def index(request):
    return render(request, "urlShortener/index.html")
def shortenUrl(request):
    url=request.POST.get('urlInput')
    urlShortener = pyshorteners.Shortener()
    newUrl= urlShortener.tinyurl.short(url)
    return render(request, "urlShortener/shortenUrl.html", {
        "shortenedUrl" :newUrl
    })