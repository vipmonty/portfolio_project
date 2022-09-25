from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    return HttpResponse("<h1>THIS IS VIPHAKONE MONTY'S BLOGS HOMEPAGE</h1 >")


def about(request):
    return HttpResponse("<h1>ABOUT VIP'S BLOG</h1>")
