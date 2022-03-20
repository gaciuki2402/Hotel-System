from django.shortcuts import render

from django.http import HttpResponse

def hotel(request):
    return HttpResponse("Welcome to 5 Star Hotel.")

# Create your views here.
