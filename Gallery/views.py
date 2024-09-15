from django.shortcuts import render
from django.views import generic, View

# Create your views here.

# Test function for Django setup
def home(request):
    return render(request, 'Gallery/home.html')