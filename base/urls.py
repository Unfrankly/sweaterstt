from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('room/<str:pk>/', room, name="room"),
    path('upid/<str:pk>/', upid, name="upid"),
    path('sdet/<str:pk>/', sdet, name="sdet"),
    # path('sdet/<str:pk>/', )
    
    ]
