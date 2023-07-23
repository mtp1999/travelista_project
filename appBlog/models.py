from django.db import models


class Post(models.Model):
    class Meta:
        db_table = 'appBlog_post'
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='appBlog/posts/images/', default='default.jpg')

    def __str__(self):
        return str(self.id) + '-' + self.title
