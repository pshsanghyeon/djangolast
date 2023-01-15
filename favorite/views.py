from django.shortcuts import render, redirect
from products.models import Products
from .models import Favorite
# Create your views here.

def favorite(request, pk):
    u = request.user
    p = Products.objects.get(id=pk)
    p.likey.add(request.user)
    
    Favorite(user=u, name= p.name, img= p.img, id= pk).save()
    
    
    return redirect("pro:detail",pk)


def unfavorite(request, pk):
    fset = Favorite.objects.all()
    p = Products.objects.get(id=pk)
    p.likey.remove(request.user)
    
    for i in fset:
        if i.id == p.id:
            i.delete()
    
    return redirect("pro:detail",pk)