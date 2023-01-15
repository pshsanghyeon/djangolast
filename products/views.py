from django.shortcuts import render
from product_kind.models import Kind
from .models import Products
# Create your views here.

def products(request):
    return render(request, 'products/products.html')

def Skin_Care(request):
    kind ="Skin_Care"
    for i in Kind.objects.all():
        if str(i) == "Skin_care":
            product_set = i.products_set.all()
    context={
        "pset":product_set,
        "kind": kind
    }
    return render(request, 'products/products.html', context)

def Face_Makeup(request):
    kind ="Face_Makeup"
    for i in Kind.objects.all():
        if str(i) == "Face_Makeup":
            product_set = i.products_set.all()
    context={
        "pset":product_set,
        "kind" : kind
    }
    return render(request, 'products/products.html', context)

def Tools(request):
    kind ="Tools & Accessories"
    for i in Kind.objects.all():
        if str(i) == "Tools_Accessories":
            product_set = i.products_set.all()
    context={
        "pset":product_set,
        "kind":kind
    }
    return render(request, 'products/products.html', context)

def Eye_Makeup(request):
    kind ="Eye_Makeup"
    for i in Kind.objects.all():
        if str(i) == "Eye_Makeup":
            product_set = i.products_set.all()
    context={
        "pset":product_set,
        "kind":kind
    }
    return render(request, 'products/products.html', context)

def Bath(request):
    kind ="Bath"
    for i in Kind.objects.all():
        if str(i) == "Bath":
            product_set = i.products_set.all()
    context={
        "pset":product_set,
        "kind":kind
    }
    return render(request, 'products/products.html', context)

def Slimming(request):
    kind ="Slimming"
    for i in Kind.objects.all():
        if str(i) == "Slimming":
            product_set = i.products_set.all()
    context={
        "pset":product_set,
        "kind":kind
    }
    return render(request, 'products/products.html', context)

def Personal_Care(request):
    kind ="Personal_Care"
    for i in Kind.objects.all():
        if str(i) == "Personal_Care":
            product_set = i.products_set.all()
    context={
        "pset":product_set,
        "kind":kind
    }
    return render(request, 'products/products.html', context)

def Hair_Care(request):
    kind ="Hair_Care"
    for i in Kind.objects.all():
        if str(i) == "Hair_Care":
            product_set = i.products_set.all()
    context={
        "pset":product_set,
        "kind":kind
    }
    return render(request, 'products/products.html', context)

def detail(request, pk):
    p = Products.objects.get(id=pk)
    rate_num = [0,0,0,0,-1]
    
    if p.rate > 0:
        if p.rate % 1 == 0:
            for i in range(0, int(p.rate)):
                rate_num[i] = i
        else:
            for i in range(0, int(p.rate)):
                rate_num[i] = i
            rate_num[i+1] = -2
    else:
        rate_num=[]
        
   
            
        
        
    context={
        "p": p,
        "rate":p.rate,
        "rate_num":rate_num
        
    }
    return render(request,'products/detail.html', context)