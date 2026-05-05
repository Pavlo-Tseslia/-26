from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Product, Category, Review, NewsletterSubscriber

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
    reviews = product.reviews.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']

    if request.method == 'POST':
        # Форма оцінювання
        if 'submit_review' in request.POST:
            rating = request.POST.get('rating')
            comment = request.POST.get('comment')
            Review.objects.create(product=product, rating=rating, comment=comment)
            return redirect('product_detail', product_id=product.id)

        # Форма підписки на розсилку
        elif 'subscribe' in request.POST:
            email = request.POST.get('email')
            NewsletterSubscriber.objects.get_or_create(email=email)
            return redirect('product_detail', product_id=product.id)

    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
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