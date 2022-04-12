from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.
def index(request):
    return render(request, "regextool/index.html")
def regCheck(request):
    text= request.POST.get('textInput')
    regex= request.POST.get('regexInput')
    result=re.findall(regex, text)
    resultpos=re.search(regex, text)
    return render(request, "regextool/result.html", {
        "result": result
        

    })