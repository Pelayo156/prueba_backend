from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogue, name="catalogue"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('dog/', views.dog, name="dog"),
    path('cat/', views.cat, name="cat"),
    path('cart/', views.cart, name="cart"),
    path('new_category/', views.new_category, name="new_category"),
    path('new_type', views.new_type, name="new_type"),
    path('new_product', views.new_product, name="new_product"),
    path('delete_category/<int:category_id>/', views.delete_category, name="delete_category"),
    path('delete_type/<int:type_id>/', views.delete_type, name='delete_type'),
    path('delete_product/<int:product_id>/', views.delete_product, name="delete_product"),
    path('edit_category/<int:category_id>/', views.edit_category, name="edit_category"),
    path('edit_type/<int:type_id>/', views.edit_type, name='edit_type'),
    path('edit_product/<int:product_id>/', views.edit_product, name="edit_product"),
]