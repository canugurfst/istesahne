from . import views
from django.urls import path

urlpatterns = [
    path('', views.video_list, name='video_list'),
]