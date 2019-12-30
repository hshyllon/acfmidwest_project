from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'), 
    path('<int:blog_id>', views.blog, name='blog'), 
    path('submission', views.submission, name='submission'), 
]