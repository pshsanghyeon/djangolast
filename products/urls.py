from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'pro'

urlpatterns = [
   path('products/', views.products, name = "products"),
   path('Skin_Care/', views.Skin_Care, name = "Skin_Care"),
   path('Face_Makeup/', views.Face_Makeup, name = "Face_Makeup"),
   path('Tools/', views.Tools, name = "Tools"),
   path('Eye_Makeup/', views.Eye_Makeup, name = "Eye_Makeup"),
   path('Bath/', views.Bath, name = "Bath"),
   path('Slimming/', views.Slimming, name = "Slimming"),
   path('Personal_Care/', views.Personal_Care, name = "Personal_Care"),
   path('Hair_Care/', views.Hair_Care, name = "Hair_Care"),
   path('detail/<pk>', views.detail, name="detail"),
]
