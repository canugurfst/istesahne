from .models import Video
from django.shortcuts import render

def video_list(request):
    videos = Video.objects.all().order_by('-created_at')

    return render(
        request,
        'videos/video_list.html',
        {'videos': videos}
    )