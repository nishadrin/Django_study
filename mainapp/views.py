from django.shortcuts import render

links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
]

def main(request):
    context = {
        'title': "главная",
    }

    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': "продукты",
        #'links_menu': links_menu,
        #'same_products': same_products
    }

    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': "контакты",
    }

    return render(request, 'mainapp/contact.html', context)
