from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200, verbose_name="Назва страви")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.title


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    session_key = models.CharField(max_length=40, null=True, blank=True)  # Для неавторизованих


class Order(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Готівка'),
        ('CARD', 'Картою при отриманні'),
        ('ONLINE', 'Оплата онлайн'),
    ]
    DELIVERY_METHODS = [
        ('PICKUP', 'Самовивіз'),
        ('COURIER', 'Доставка кур`єром'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_METHODS)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)