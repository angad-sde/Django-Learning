from django.shortcuts import render
from django.http import HttpResponse

def simple_hello(request):
    return HttpResponse("<h1>Hello, world! You are at the index page.</h1>")

def home_view(request):
    context = {
        "title": "Welcome to My Site",
        "items": ["Python", "Django", "Web Development"],
    }
    
    return render(request, "myapp/home.html", context)
