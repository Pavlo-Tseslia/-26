from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Product, Order, CartItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CartItem)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created_at', 'updated_at')
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'total_price', 'created_at')