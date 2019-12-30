from django.urls import path
from . import views

urlpatterns = [
    path('', views.ministries, name='ministries'),  
    path('missions', views.missions, name='missions'),  
    path('cministry', views.cministry, name='cministry'), 
    path('aministry', views.aministry, name='aministry'), 
    path('yministry', views.yministry, name='yministry'), 
    
]