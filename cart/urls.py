from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "cart"

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("remove/<ipk>", views.remove, name="remove"),
    path('addcart/<ipk>', views.addcart, name="addcart"),
    path('buy/', views.buy, name="buy"),
    path('points/', views.points, name="points"),
    path('xpoints/', views.xpoints, name="xpoints"),
   
   
]