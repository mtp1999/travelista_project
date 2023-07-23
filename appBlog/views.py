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
    post_id_list = [post.id for post in Post.objects.all().filter(status=1)]
    post_id_list.sort()
    post = Post.objects.get(id=pid)
    try:
        next_post = Post.objects.get(id=post_id_list[post_id_list.index(pid)+1])
    except:
        next_post = None
    try:
        if post_id_list.index(pid) - 1 == -1:
            raise ValueError
        previous_post = Post.objects.get(id=post_id_list[post_id_list.index(pid) - 1])
    except:
        previous_post = None
    try:
        post.views += 1
        post.save()
    except:
        return redirect('appBlog:home')
    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post
    }
    return render(request, 'appBlog/blog-single.html', context)