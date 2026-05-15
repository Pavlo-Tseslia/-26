import random
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login # Додано для автоматичного входу
from .models import Product, Category, Order
from django.contrib.admin.views.decorators import staff_member_required

# Головна сторінка
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:6]
    return render(request, 'catalog/index.html', {
        'categories': categories,
        'products': products,
        'title': 'Ласкаво просимо до Bella Italia'
    })

# Меню ресторану
def menu(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'catalog/menu.html', {
        'categories': categories,
        'products': products,
        'title': 'Наше Меню',
        'total_price': total_price
    })

# Перегляд кошика
def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'catalog/cart.html', {
        'cart': cart,
        'total_price': total_price
    })

# Додавання у кошик
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    if p_id in cart:
        cart[p_id]['quantity'] += 1
    else:
        cart[p_id] = {
            'title': product.title,
            'price': str(product.price),
            'quantity': 1
        }
    request.session['cart'] = cart
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER', 'menu'))

# Видалення з кошика
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    if p_id in cart:
        if cart[p_id]['quantity'] > 1:
            cart[p_id]['quantity'] -= 1
        else:
            del cart[p_id]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER', 'view_cart'))

# Оформлення замовлення
@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        if not cart:
            return redirect('menu')

        items_list = [f"{item['title']} (x{item['quantity']})" for item in cart.values()]
        items_str = ", ".join(items_list)
        total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

        new_order = Order.objects.create(
            user=request.user,
            items_json=items_str,
            total_price=total_price,
            delivery_type=request.POST.get('delivery_type', 'delivery'),
            status='pending'
        )

        # Очищаємо кошик
        request.session['cart'] = {}
        request.session.modified = True

        return render(request, 'catalog/success.html', {'order_number': new_order.id})

    return render(request, 'catalog/checkout.html', {'cart': cart})

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status == 'pending':
        order.status = 'cancelled'
        order.save()
    return redirect('profile')

# Сторінки "Про нас" та "Контакти"
def about(request):
    return render(request, 'catalog/about.html', {'title': 'Про нас'})

def contact(request):
    return render(request, 'catalog/contact.html', {'title': 'Контакти'})

# --- НОВИЙ ТА ОНОВЛЕНИЙ КОД ---

# Реєстрація (Оновлено: додано автоматичний вхід)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Користувач відразу входить після реєстрації
            return redirect('menu') # Після реєстрації ведемо на меню
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Профіль
@login_required
def profile(request):
    if request.user.username == 'bob' or request.user.is_staff:
        orders = Order.objects.all().order_by('-created_at')
    else:
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'catalog/profile.html', {'orders': orders})

# Оновлення статусу для Боба
@login_required
def update_order_status(request, order_id):
    if request.user.username == 'bob' or request.user.is_staff:
        order = get_object_or_404(Order, id=order_id)
        if request.method == 'POST':
            order.status = request.POST.get('new_status')
            order.save()
    return redirect('profile')