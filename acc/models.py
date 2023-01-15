from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    img = models.ImageField(null=True)
    
    def getpic(self):
        if self.img:
            return self.img.url
        return "/media/noimage.jpg"
    
    
    
