from django.shortcuts import render, get_object_or_404
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
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    user_name = request.user

    product_list = Product.objects.all()
    print("Имя пордукта: ", product_list)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}

        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_main_menu': links_main_menu,
            'links_menu': links_menu,
            'category': category,
            'products': products,
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
