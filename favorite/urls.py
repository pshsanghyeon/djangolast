from django.contrib import admin
from django.urls import path, include
from . import views
app_name="favorite"
urlpatterns = [
    path('favorite/<pk>', views.favorite, name="favorite"),
    path('unfavorite/<pk>', views.unfavorite, name="unfavorite"),
    
]