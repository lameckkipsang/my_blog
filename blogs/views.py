from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def intro(request):
    student = {
        "school":"School: Zindua School",
        "name":"Name: Lameck",
        "email":"Email: lameck.cs16@gmail.com"
    }
    return render(request, 'intro.html', student)
def home(request):
    student = {
        "school":"Zindua School",
        "name":"Lameck Kipsang",
        "email":"lameck.cs16@gmail.com"
    }
    return render(request, 'index.html', student)

def contact(request):
    contact_details = {
        "email": "lameck.cs16@gmail.com",
        "number": "+254725713859"
    }
    return render(request, 'contact.html', contact_details)

def about(request):
    about_details = {
        "name": "Zindua School",
        "location": "Parklands Plaza, Westlands",
        "course": "Software Engineering"
    }
    return render(request, 'about.html', about_details)

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {"posts": posts})

def blog_detail(request, slug):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog_detail.html', {"post":post})