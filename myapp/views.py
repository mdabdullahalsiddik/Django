from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return HttpResponse("Md Abdullah Al Siddik")

def profile(request):
    return HttpResponse("Profile")

def about (request):
    return render(request,template_name= 'about.html')
def service (request):
    return render(request,template_name= 'service.html')