from django.contrib import admin
from appBlog.models import Post, Category, Contact, Comment
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Comment)
