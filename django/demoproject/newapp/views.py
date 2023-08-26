from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("This is the new application created.")

def myview(request):

    return HttpResponsePermanentRedirect(reverse('demoapp:login'))