from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('dog/', views.dog, name="dog"),
    path('cat/', views.cat, name="cat"),
    path('cart/', views.cart, name="cart")
]