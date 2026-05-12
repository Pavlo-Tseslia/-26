from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Category, CartItem, Order


# Головна сторінка
def index(request):
    categories = Category.objects.all()
    featured_products = Product.objects.all()[:6]
    return render(request, 'catalog/index.html', {
        'categories': categories,
        'products': featured_products,
        'title': 'Ласкаво просимо до Bella Italia'
    })


# Меню ресторану
def menu(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'catalog/menu.html', {
        'categories': categories,
        'products': products,
        'title': 'Наше Меню'
    })


# Додавання у кошик
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Перевіряємо сесію, якщо користувач не залогінений
    if not request.session.session_key:
        request.session.create()

    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        user=request.user if request.user.is_authenticated else None,
        session_key=request.session.session_key if not request.user.is_authenticated else None
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')


# Перегляд кошика
def view_cart(request):
    if request.user.is_authenticated:
        items = CartItem.objects.filter(user=request.user)
    else:
        items = CartItem.objects.filter(session_key=request.session.session_key)

    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'catalog/cart.html', {'items': items, 'total': total})


# Оформлення замовлення
def checkout(request):
    if request.method == 'POST':
        return render(request, 'catalog/success.html')
    return render(request, 'catalog/checkout.html')


# Сторінки "Про нас" та "Контакти"
def about(request):
    return render(request, 'catalog/about.html', {'title': 'Про нас'})


def contact(request):
    return render(request, 'catalog/contact.html', {'title': 'Контакти'})


# --- НОВИЙ КОД: Реєстрація та Профіль ---

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    # Адмін бачить всі замовлення, користувач — тільки свої
    if request.user.is_staff:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)
    return render(request, 'catalog/profile.html', {'orders': orders})