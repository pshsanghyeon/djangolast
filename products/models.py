from django.db import models
from product_kind.models import Kind
from acc.models import User
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=100, blank=True)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    skin_type= models.CharField(max_length=100, blank=True)
    skin_care_benefits= models.CharField(max_length=100, blank=True)
    size= models.CharField(max_length=100, blank=True)
    condition= models.CharField(max_length=100, blank=True)
    shelf= models.CharField(max_length=100, blank=True)
    country= models.CharField(max_length=100, blank=True)
    expiry_date= models.CharField(max_length=100, blank=True)
    stock= models.CharField(max_length=100, blank=True)
    ship= models.CharField(max_length=100, blank=True)
    Description = models.TextField(blank = True)
    img = models.ImageField(null=True)
    likey = models.ManyToManyField(User, null=True)

    
    def __str__(self):
        return f"{self.kind}_{self.name}"
    