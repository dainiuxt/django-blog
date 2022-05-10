from django.shortcuts import render, reverse, redirect
from blog.models import BlogPost, Comment

def index(request):
    all_posts = BlogPost.objects.all()
    context = {
      'all_posts': all_posts,
    }
    return render(request, 'index.html', context=context)
