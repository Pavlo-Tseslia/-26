from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Головні сторінки
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Меню та кошик
    path('menu/', views.menu, name='menu'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),

    # Акаунт та реєстрація
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),

    # Стандартні шляхи для входу/виходу (Django auth)
    path('', include('django.contrib.auth.urls')),
]