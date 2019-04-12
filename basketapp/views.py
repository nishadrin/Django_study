from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from .models import Basket


def basket(request):
    return render(request, 'basketapp/basket.html')


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = request.user.basket.filter(product=pk).first()

    if basket:
        basket.quantity += 1
        basket.save()
    else:
        new_basket = Basket(user=request.user, product=product)
        new_basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = request.user.basket.filter(product=pk).first()

    if basket:
        if basket.quantity > 1:
            basket.quantity -= 1
            basket.save()
        else:
            basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
