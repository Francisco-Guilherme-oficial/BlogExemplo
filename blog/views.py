from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": Post.objects.get(pk=post_id)
    }
    return render(request, "post.html", context)

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
