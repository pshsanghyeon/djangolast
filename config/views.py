from django.shortcuts import render, redirect
from products.models import Products
from cart.models import Cart



def home(request):
    return render(request,'home.html')

def buynow(request, pk):
    p = Products.objects.get(id=pk)
    Cart(name = p.name, price = p.price, quantity= 1, img = p.img, user=request.user).save()
    return redirect("cart:cart")