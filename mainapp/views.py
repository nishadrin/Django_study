from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ProductCategory, Product
from basketapp.models import Basket
import random
from django.conf import settings
from django.core.cache import cache

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


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')


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
    products = get_products()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(is_active=True, category__is_active=True,category=hot_product.category).exclude(pk=hot_product.pk).select_related('category')[:3]

    return same_products


def products(request, pk=None, page=1):
    title = "продукты"
    links_menu = get_links_menu()
    user_name = request.user

    product_list = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')

    if pk is not None:
        if pk == 0:
            category = {'pk': 0, 'name': 'все'}
            products = get_products_orederd_by_price()

        else:
            category = get_category(pk)
            products = get_products_in_category_orederd_by_price(pk)

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
    links_menu = get_links_menu()
    product = get_product(pk)

    content = {
        'title': title,
        'links_main_menu': links_main_menu,
        'links_menu': links_menu,
        'product': product,
        'basket': get_basket(request.user),
        'user_name': user_name,
    }
    return render(request, 'mainapp/product.html', content)


def contact(request):
    title = "контакты"
    user_name = request.user

    if settings.LOW_CACHE:
        key = f'locations'
        locations = cache.get(key)
        if locations is None:
            locations = load_from_json('contact__locations')
            cache.set(key, locations)
    else:
        locations = load_from_json('contact__locations')

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
        'user_name': user_name,
        'locations': locations,
    }

    return render(request, 'mainapp/contact.html', context)


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', errors='ignore') as infile:
        return json.load(infile)
