from django.db import models
from acc.models import User
# Create your models here.


class Cart(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    img = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.user}_{self.name}"