from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def poll(request):
    return HttpResponse("I am polling~")

def main(request):

	return HttpResponse("This is the main page for poll application.")