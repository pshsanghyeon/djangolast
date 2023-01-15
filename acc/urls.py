from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "acc"

urlpatterns = [
   path('signup/', views.signup, name="signup"),
   path('profile/', views.profile, name ="profile"),
   path('login/', views.ulogin, name="login"),
   path('logout/', views.ulogout, name="logout"),
   path('update/', views.update, name="update"),
   path('ckpass', views.ckpass, name="ckpass"),
   path('delete', views.delete, name="delete"),
   
   
]