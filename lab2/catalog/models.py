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

# Модель оформленого замовлення (для історії в кабінеті)
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Клієнт")
    items_json = models.TextField(verbose_name="Склад замовлення")  # Тут буде список: "Піца x2, Кола x1"
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сума")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення #{self.id} - {self.user.username}"