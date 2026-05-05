from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
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