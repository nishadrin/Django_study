from django.shortcuts import render, get_object_or_404
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
    basket = request.user.basket.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}

        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_main_menu': links_main_menu,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
            'user_name': user_name
        }

        return render(request, 'mainapp/products_list.html', context)

    same_products = Product.objects.all()[0:10]

    context = {
        'title': title,
        'links_main_menu': links_main_menu,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket,
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
