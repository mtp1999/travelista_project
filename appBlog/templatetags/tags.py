from django import template
from appBlog.models import Category, Post, Comment

register = template.Library()


@register.inclusion_tag('appBlog/_blog-category-section.html')
def categories():
    cat_dict = {}
    for category in Category.objects.all():
        cat_dict[category.name] = category.post_set.filter(status=1).count()
    return {'categories': cat_dict.items()}


@register.inclusion_tag('appBlog/_blog-latest-posts-section.html')
def latest_posts(number=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:number]
    return {'posts': posts}


@register.inclusion_tag('appBlog/_blog-last-6-posts.html')
def last_6_posts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:6]
    return {'posts': posts}


@register.simple_tag
def counting_post_comments(post_id):
    return Comment.objects.filter(post=post_id, allowed=True).count()
