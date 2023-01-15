from django.shortcuts import render, redirect
from .models import Cart
from products.models import Products
from django.contrib import messages
# Create your views here.

def xpoints(request):
    u = request.user
    u.points = -(u.points)
    u.save()
    return redirect("cart:cart")



def points(request):
    u = request.user
    cset = u.cart_set.all()
    total = 0
    button = 0
    for i in cset:
            total += float(i.price)
    context={
        "cset":cset,
        "total":total,
        
    }
    if u.points > 0:
        total = round(((10 - u.points) / 10) * float(total), 4)
        context.update({
            "total":total,
            "button":button,
        })
        messages.add_message(request, messages.SUCCESS, f'Your {u.points} points are used!' )
        u.points = (-u.points)
        u.save()
    else:
        messages.add_message(request, messages.ERROR, f'You do not have any points!' )
    return render(request,'cart/cart.html', context)


def buy(request):
    u = request.user
    cset = Cart.objects.all()
    total = 0
    for i in cset:
        total += 1
    if int(u.points) >= 0:
        u.points += total
        u.save()
    else:
        u.points = 0
        u.points += total
        u.save()
    if cset:
        cset.delete()
    else:
        messages.add_message(request, messages.ERROR, 'No items in your cart!')
        return redirect('cart:cart')
    messages.add_message(request, messages.SUCCESS, 'Ordered Complete!')
    return redirect('home')


def addcart(request, ipk):
    u = request.user
    p = Products.objects.get(id=ipk)
    num = request.GET.get("quantity")
    if int(num) > 1:
        p.price = round(float(p.price) * int(num), 4)
        Cart(name=p.name, price=p.price, quantity=num, img=p.img, user=u).save()    
    else:
        Cart(name=p.name, price=p.price, quantity=num, img=p.img, user=u).save()    
    
    return redirect('pro:Skin_Care')



def remove(request, ipk):
    p = Cart.objects.get(id=ipk)
    p.delete()
    return redirect("cart:cart")
    
    
def cart(request):
    u = request.user
    cset = u.cart_set.all()
    total = 0
    
    for i in cset:
        total += round(float(i.price), 4)
        
    total = round(total, 4)
    context={
        "cset":cset,
        "total":total
    }
    
    
    return render(request,'cart/cart.html', context)