from django.shortcuts import render
# from django.http import HttpResponse
import random

def home(request): 
 return render(request, 'generador/home.html')

def about(request): 
 return render(request, 'generador/about.html')

def password(request): 

 characters = list('abcdefghijklmnopqrstuvwxyz')

 if request.GET.get('uppercase'):
  characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

 if request.GET.get('numbers'):
  characters.extend(list('0123456789'))

 if request.GET.get('special'):
  characters.extend(list('!@#$%^&*-()_+'))

 length = int(request.GET.get('length', 12))

 generated_password = ''
 for x in range(length):
  generated_password += random.choice(characters)
 return render(request, 'generador/password.html', {'password': generated_password})
