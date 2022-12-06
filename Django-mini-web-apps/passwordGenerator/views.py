from django.shortcuts import render
import random
import string
def index(request):
    return render(request, "passwordGenerator/index.html")
def generatePassword(request):
    password= ''
    characters= list(string.ascii_letters+string.digits+"!£$@#")
    random.shuffle(characters)
    for i in range(9):
        password+=characters[i]
    return render(request, "passwordGenerator/index.html", {
        "password": password
    })