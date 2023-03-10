from django.db import models

from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    description = models.TextField(blank=True)
    
    nickname = models.CharField(max_length = 40, blank=True)
    
    image = models.ImageField(default='home/static/images/default.jpg', upload_to='profile_pictures')
