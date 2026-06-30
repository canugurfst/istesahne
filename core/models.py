from django.db import models

# Create your models here.
class PageContent(models.Model):
    page = models.CharField(max_length=20)

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class SiteLogo(models.Model):
    image = models.ImageField(upload_to="logos/")
    alt_text = models.CharField(max_length=100, default="Iste Sahne Logo")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.alt_text