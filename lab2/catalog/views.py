from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'catalog/index.html', {'title': 'Головна сторінка'})

def about(request):
    return render(request, 'catalog/about.html', {'title': 'Про нас'})

def contact(request):
    return render(request, 'catalog/contact.html', {'title': 'Контакти'})