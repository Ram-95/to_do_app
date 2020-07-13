from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'to_do_app/home.html')

def test(request):
    return render(request, 'to_do_app/test.html')
