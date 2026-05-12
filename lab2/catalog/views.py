from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, CartItem, Order
from django.contrib.auth.decorators import login_required


def index(request):
    categories = Category.objects.all()
    featured_products = Product.objects.all()[:6]  # Популярні страви
    return render(request, 'catalog/index.html', {
        'categories': categories,
        'products': featured_products,
        'title': 'Ласкаво просимо до Bella Italia'
    })


def menu(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'catalog/menu.html', {
        'categories': categories,
        'products': products,
        'title': 'Наше Меню'
    })


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        user=request.user if request.user.is_authenticated else None,
        session_key=request.session.session_key if not request.user.is_authenticated else None
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')


def view_cart(request):
    if request.user.is_authenticated:
        items = CartItem.objects.filter(user=request.user)
    else:
        items = CartItem.objects.filter(session_key=request.session.session_key)

    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'catalog/cart.html', {'items': items, 'total': total})


def checkout(request):
    if request.method == 'POST':
        # Тут буде логіка збереження замовлення
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        payment = request.POST.get('payment')
        delivery = request.POST.get('delivery')

        # Створюємо замовлення (спрощено)
        return render(request, 'catalog/success.html')

    return render(request, 'catalog/checkout.html')