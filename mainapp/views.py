from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")

def pricing(request):
    return render(request,"pricing.html")    


def contact(request):
    return render(request,"contact.html")  

def team(request):
    return render(request,"team.html")  
