from django.shortcuts import render, reverse, redirect
from blog.models import BlogPost, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    post_list = BlogPost.objects.all()
    page = request.GET.get('page', 1)
    # context = {
    #   'post_list': post_list,
    # }
    paginator = Paginator(post_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts': posts})
