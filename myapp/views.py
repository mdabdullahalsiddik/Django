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
    data ={
        "title" : "Service",
        "services" : ["Service 1","Service 2","Service 3"],
        "description" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel ex at diam faucibus malesuada. Nulla facilisi. Sed euismod orci ac neque aliquam, vitae ultricies felis commodo. Sed consectetur, felis sit amet ullamcorper consectetur, lectus nunc lobortis arcu, in tristique felis ligula in nulla.",
  
        
    }
    return render(request,'service.html', data)