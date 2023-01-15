from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from cart.models import Cart
from favorite.models import Favorite
# Create your views here.


def delete(request):
    u = request.user
    if request.method == "POST":
        pw = request.POST.get("pass")
        if check_password(pw, u.password):
            u.delete()
            return redirect("home")
        else:
            messages.add_message(request, messages.ERROR, 'the password is incorrect!')
    return redirect("acc:profile")


def ckpass(request):
    if request.method == "POST":
        u = request.user
        pw = request.POST.get("pass")
        new = request.POST.get("new")
        if check_password(pw, u.password):
            u.set_password(new)
            u.save()
            logout(request)
            return redirect('acc:login')
        else:
            messages.add_message(request, messages.ERROR, 'the password is incorrect!')
        
        
    return redirect('acc:profile')


def ulogin(request):
    if request.method == "POST":
        ui = request.POST.get("ID")
        up = request.POST.get("pass")
        user = authenticate(username=ui, password=up)
        print(user)
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.add_message(request, messages.ERROR, 'id does not exist or password is incorrect!')
    return render(request, 'user/login.html')


def ulogout(request):
    logout(request)
    return redirect("home")

def profile(request):
    u = request.user
    pset = u.favorite_set.all()
        
    context={
        "pset":pset
        
    }
    return render(request, 'user/profile.html', context)

def signup(request):
    uset = User.objects.all()
    total = 0
    phone_total = 0
    if request.method == "POST":
        ui = request.POST.get("ID")
        up = request.POST.get("pass")
        ckp = request.POST.get("ckpass")
        phone = request.POST.get("phone")
        uim = request.FILES.get("img")
        
        for i in up:
            total += 1
        for j in phone:
            phone_total += 1
            
        for g in User.objects.all():
            if ui == g.username:
                messages.add_message(request, messages.ERROR, 'User ID already exists!')
                return render(request,'user/signup.html')
            else:
                pass
                
        if total >= 10:
            if up == ckp:
                if phone_total == 11:
                    for i in uset:
                        if not phone in i.phone:
                            User.objects.create_user(username=ui, password=up, phone=phone, img=uim)
                            return redirect("acc:login")
                        else:
                            messages.add_message(request, messages.ERROR, 'phone number already exists!')
                else:
                    messages.add_message(request, messages.ERROR, 'phone number is strange!')
            else:
                messages.add_message(request, messages.ERROR, 'password should be the same!')
        else:
            messages.add_message(request, messages.ERROR, 'password should be longer than 10!')
    
    return render(request,'user/signup.html')


def update(request):
    if request.method =="POST":
        u = request.user
        phone = request.POST.get("phone")
        img = request.FILES.get("img") 
        u.phone = phone
        print(img)
        
        if img:
            u.img.delete()
            u.img = img
        u.save()
        return redirect("acc:profile")
        
    return render(request, 'user/update.html')