from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts': posts})