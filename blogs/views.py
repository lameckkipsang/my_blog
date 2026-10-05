from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# def hello(request):
#     return HttpResponse("Hello World!")

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

def blog_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_detail.html', {"post":post})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # Assign the currently logged-in user.
            post.user = request.user
            post.save()
            return redirect("blog_detail", post_id=post.id)
    else:
        form = PostForm()

    return render(
        request,
        "post_form.html",
        {
            "form": form,
            "page_title": "Create Post",
            "button_text": "Publish Post",
        },
    )


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Only the author can edit the post.
    if post.user != request.user:
        return redirect("blog_detail", post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_detail", post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "post_form.html",
        {
            "form": form,
            "page_title": "Edit Post",
            "button_text": "Update Post",
            "post": post,
        },
    )