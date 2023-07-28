from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return str(self.id) + '-' + self.title


class Category(models.Model):
    class Meta:
        db_table = 'appBlog_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

