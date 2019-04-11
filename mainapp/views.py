from django.shortcuts import render
from .models import ProductCategory, Product

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
    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
    }

    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = "продукты"

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
        #'same_products': same_products
    }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    title = "контакты"

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
    }

    return render(request, 'mainapp/contact.html', context)
