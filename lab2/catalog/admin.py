from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Product, Order, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Залишаємо тільки ті поля, які є в моделі Category у вашому models.py
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Поля, які точно є в моделі Product
    list_display = ('title', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Поля моделі Order
    list_display = ('full_name', 'payment_method', 'delivery_method', 'total_price', 'created_at')
    list_filter = ('payment_method', 'delivery_method')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'user')