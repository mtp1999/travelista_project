from django.shortcuts import render, redirect
from appBlog.models import Post
from django.utils import timezone

"""
use admin by:
username: admin1
password: admin1
"""


def home(request):

    date_time_now = timezone.now()
    posts = Post.objects.filter(published_date__lte=date_time_now, status=1)

    context = {
        'posts': posts,
    }
    return render(request, 'appBlog/blog-home.html', context)


def single(request, pid):
    post = Post.objects.get(id=pid)
    try:
        post.views += 1
        post.save()
    except:
        return redirect('appBlog:home')
    context = {
        'post': post
    }
    return render(request, 'appBlog/blog-single.html', context)