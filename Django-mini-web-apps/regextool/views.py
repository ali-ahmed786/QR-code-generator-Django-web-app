from shutil import register_unpack_format
from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.
def index(request):
    return render(request, "regextool/index.html")
def regCheck(request):
    text= request.POST.get('textInput')+''
    regex= r''+request.POST.get('regexInput')+''
    try:
        re.compile(regex)
        result=re.findall(regex, text)
        newResult= list( dict.fromkeys(result) )
        if len(newResult)==0:
            text="No matching patterns found!!"
        resultpos=re.search(regex, text)
        return render(request, "regextool/result.html", {
        "text": text.split(),
        "result": newResult,
        "regin": regex
    })
    except:
         return render(request, "regextool/index.html", {
        "text": "Please enter a valid regular expression!",
 
    })

