from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Md Abdullah Al Siddik")

def profile(request):
    return HttpResponse("Profile")