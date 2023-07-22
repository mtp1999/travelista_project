from django.urls import path
from appBlog import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'appBlog'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pid>/', views.single, name='single'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)