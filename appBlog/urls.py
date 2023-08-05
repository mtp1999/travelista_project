from django.urls import path
from appBlog import views
from django.conf import settings
from django.conf.urls.static import static
from appBlog.feeds import LatestEntriesFeed
app_name = 'appBlog'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/category/<str:category>/', views.post_list_view, name='post_list_category'),
    path('posts/tag/<str:tag>/', views.post_list_view, name='post_list_tag'),
    path('posts/author/<str:author>/', views.post_list_view, name='post_list_author'),
    path('posts/<int:pid>/', views.single_post_view, name='single'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    path('rss/feed/', LatestEntriesFeed()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)