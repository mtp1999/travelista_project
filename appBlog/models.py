from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    class Meta:
        db_table = 'appBlog_post'
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='appBlog/posts/images/', default='default.jpg')
    categories = models.ManyToManyField('Category', db_table='appBlog_post_category')
    tags = TaggableManager()

    def __str__(self):
        return str(self.id) + '-' + self.title

    def get_absolute_url(self):
        return reverse('appBlog:single', kwargs={'pid': self.id})


class Category(models.Model):
    class Meta:
        db_table = 'appBlog_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    allowed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + '-' + self.subject
