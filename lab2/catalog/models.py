from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Модель категорій страв
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.name

# Модель самих страв (піца, паста тощо)
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категорія")
    title = models.CharField(max_length=200, verbose_name="Назва страви")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Фото (файл)")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Посилання на фото (URL)")

    def __str__(self):
        return self.title

# Модель для збереження товарів у кошику (до оформлення)
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    session_key = models.CharField(max_length=40, null=True, blank=True)

# ОБ'ЄДНАНА МОДЕЛЬ ЗАМОВЛЕННЯ (Тепер лише одна версія)
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Прийнято'),
        ('preparing', 'Готується'),
        ('delivering', 'В дорозі (Кур\'єр)'),
        ('ready', 'Готово до видачі'),
        ('completed', 'Виконано'),
        ('cancelled', 'Скасовано'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name="Клієнт")
    items_json = models.TextField(verbose_name="Склад замовлення")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сума")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    delivery_type = models.CharField(max_length=20, default='delivery', verbose_name="Тип доставки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        # Додано перевірку на випадок, якщо username недоступний
        username = self.user.username if self.user else "Гість"
        return f"Замовлення #{self.id} - {username}"