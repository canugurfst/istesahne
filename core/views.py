from core.models import PageContent
from django.shortcuts import render
from videos.models import Video

def home(request):
    page = PageContent.objects.filter(page="home").first()

    latest_videos = Video.objects.order_by('-created_at')[:3]

    return render(
        request, 
        'core/home.html',
        {
            'page': page,
            'latest_videos': latest_videos,
        }
    )

def about(request):
    page = PageContent.objects.get(page="about")
    return render(request, "core/about.html", {"page": page})

def contact(request):
    page = PageContent.objects.get(page="contact")
    return render(request, "core/contact.html", {"page": page})