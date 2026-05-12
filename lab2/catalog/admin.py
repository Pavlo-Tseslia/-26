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
    # Використовуємо лише ті поля, які є у вашій новій моделі Order
    list_display = ('id', 'user', 'total_price', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username', 'items_json')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'user')