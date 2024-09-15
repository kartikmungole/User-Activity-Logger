from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")

def about(request):
    return HttpResponse("About us page")

def contact(request):
    return HttpResponse("Contact page")

