from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ProductCategory, Product
from basketapp.models import Basket
import random

links_main_menu = [
{
    'href': 'main', 'name': 'Главная'
},
{
    'href': 'products:index', 'name': 'Каталог'
},
{
    'href': 'contact', 'name': 'Контакты'
}
]


def main(request):
    title = 'главная'
    user_name = request.user

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
        'user_name': user_name
    }

    return render(request, 'mainapp/index.html', context)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.filter(is_active=True, category__is_active=True)

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(is_active=True, category__is_active=True,category=hot_product.category).exclude(pk=hot_product.pk).select_related('category')[:3]

    return same_products


def products(request, pk=None, page=1):
    title = "продукты"
    links_menu = ProductCategory.objects.filter(is_active=True)
    user_name = request.user

    product_list = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')

    if pk is not None:
        if pk == 0:
            category = {'pk': 0, 'name': 'все'}
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')

        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_main_menu': links_main_menu,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'user_name': user_name
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    print(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'links_main_menu': links_main_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'user_name': user_name
    }

    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'продукты'
    user_name = request.user

    content = {
        'title': title,
        'links_main_menu': links_main_menu,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
        'user_name': user_name,
    }
    return render(request, 'mainapp/product.html', content)


def contact(request):
    title = "контакты"
    user_name = request.user

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
        'user_name': user_name
    }

    return render(request, 'mainapp/contact.html', context)


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', errors='ignore') as infile:
        return json.load(infile)
