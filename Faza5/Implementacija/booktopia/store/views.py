from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def categories(request):
    categories = Category.objects.all()  # uzima sve kategorije sa databeze
    context = {
        'categories': categories
    }
    return context


def all_products(request):
    products = Product.objects.filter(is_active=True)
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context)


def product_detail(request, slug):
    book = get_object_or_404(Product, slug=slug, in_stock=True)
    context = {
        'product': book
    }
    return render(request, 'store/products/detail.html', context)

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug) # we select 1 item from the databaase, Category table
    products = Product.objects.filter(category=category)
    context = {
        'category':category,
        'products':products,
    }
    return render(request, 'store/products/category.html', context)
