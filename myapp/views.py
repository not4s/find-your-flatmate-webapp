import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("<h1>Find Your Ideal Flatmate!")
    #return render(request, homepage.html)

