from multiprocessing import context
from turtle import pos
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


posts = [
    {
        'author': 'Viphakone',
        'title': 'Blog Post 1',
        'content': 'Today I shot an Eagle.',
        'date_posted': 'September 19th, 2022',
    },
    {
        'author': 'Booger Face Monster',
        'title': 'Blog Post 2',
        'content': 'I watch a dog eat a rat.',
        'date_posted': 'September 19th, 2022',
    }
]


def home_page(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
