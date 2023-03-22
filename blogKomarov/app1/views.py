from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def detail(request,id):
  posts = Post.objects.get(id=id)
  return render(request, 'details.html', {'posts': posts})

