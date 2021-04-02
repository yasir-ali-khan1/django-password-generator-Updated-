from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'home.html')
def password(request):
    password1='testing'

    character=list('abcdefghijklmnopqrstuvwxyz')
    length1=int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*();:,.'))
    if request.GET.get('number'):
        character.extend(list('0123456789'))
    password=''
    for i in range(length1):
        password += random.choice(character)

    return render(request,'password.html',{'password':password})