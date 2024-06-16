from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    testpassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(length):
        testpassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': testpassword})

def about(request):
    return render(request, 'generator/about.html')