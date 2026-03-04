from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # simple response; replace with a template later
    return HttpResponse("<h1>Welcome to the Lake project!</h1>")
