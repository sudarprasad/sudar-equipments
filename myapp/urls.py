from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('products/', views.products),
    path('services/', views.services),
    path('contact/', views.contact),
]