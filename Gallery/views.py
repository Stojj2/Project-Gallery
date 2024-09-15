from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.

# Test function for Django setup
def say_hello(request):
    return HttpResponse("Hello! Django seems to work just fine.")