from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
]