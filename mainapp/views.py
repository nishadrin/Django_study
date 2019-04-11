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
    user_name = request.user

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
        'user_name': user_name
    }

    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    title = "продукты"
    links_menu = ProductCategory.objects.all()
    user_name = request.user

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
        'links_menu': links_menu,
        'user_name': user_name
    }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    title = "контакты"
    user_name = request.user

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
        'user_name': user_name
    }

    return render(request, 'mainapp/contact.html', context)
