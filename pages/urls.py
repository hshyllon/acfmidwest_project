from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'), 
    path('volunteer', views.volunteer, name='volunteer'), 
    path('gallery', views.gallery, name='gallery'),  
    path('gallery/<int:album_id>', views.photo, name='photo'),
    path('history', views.history, name='history'),  
    
    
    #    url(r'^(?P<happeningdetail_type>[\w+]+)/(?P<happeningdetail_id>[0-9]+)/happeningdetail$', views.happeningdetail , name='happeningdetail'), 
]