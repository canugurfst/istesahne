from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    youtube_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def youtube_id(self):
        if "v=" in self.youtube_url:
            return self.youtube_url.split("v=")[1].split("&")[0]
        return ""
    
