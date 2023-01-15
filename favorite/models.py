from django.db import models
from acc.models import User
from products.models import Products
# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    img = models.ImageField(null=True)
    
    def __str__(self):
        return f"{self.user}_{self.name}"