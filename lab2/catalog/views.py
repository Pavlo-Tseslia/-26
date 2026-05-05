from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'catalog/index.html', {
        'categories': categories,
        'products': products,
        'title': 'Головна сторінка'
    })

def about(request):
    return render(request, 'catalog/about.html', {'title': 'Про нас'})

def contact(request):
    return render(request, 'catalog/contact.html', {'title': 'Контакти'})

# Детальна сторінка конкретного товару
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'title': product.title
    })

# Сторінка товарів певної категорії
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'catalog/category_products.html', {
        'category': category,
        'products': products,
        'title': category.name
    })