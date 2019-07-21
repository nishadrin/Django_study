from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from basketapp.models import Basket
from mainapp.views import links_main_menu as links_main_menu
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('product__category').select_related("product")

        content = {
            'basket_items': basket_items,
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html',content)

        return JsonResponse({'result': result})


@login_required
def basket(request):
    title = 'корзина'
    user_name = request.user
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category').select_related("product")

    context = {
        'title': title,
        'basket_items': basket_items,
        'links_main_menu': links_main_menu,
        'user_name': user_name
    }

    return render(request, 'basketapp/basket.html', context)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)
        basket.quantity = 0

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



    # product = get_object_or_404(Product, pk=pk)
    # basket = request.user.basket.filter(product=pk).first()
    #
    # if basket:
    #     if basket.quantity > 1:
    #         basket.quantity -= 1
    #         basket.save()
    #     else:
    #         basket.delete()
    #
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # Лучше использовать не метод delete(), а создать в модели доп. атрибут - флаг active
    # В перспективе необходимо добавить механизм подтверждения с формой и передачей данных методом POST (а значит, и защитой CSRF).
