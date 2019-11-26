from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from basketapp.models import Basket
from mainapp.models import Product
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def index(request):
    return render(request, 'basketapp/basket.html')

@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('main:product', kwargs={'product_pk': pk}))

    product = get_object_or_404(Product, pk=pk)

    old_basket_item = Basket.objects.filter(user=request.user, product=product).first()

    if old_basket_item:
        old_basket_item.quantity += 1
        old_basket_item.save()
    else:
        new_basket_item = Basket(user=request.user, product=product)
        new_basket_item.quantity += 1
        new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_add_ajax(request, pk, value):
    if request.is_ajax():

                # print(f'данные получены аяксом: {pk}, {value}')
        basket_item = Basket.objects.filter(pk=pk).first()
        if basket_item:
            value = int(value)
            if value > 0:
                basket_item.quantity = value
                basket_item.save()
            else:
                basket_item.delete()

        context = {
            'basket': request.user.basket_set.all().order_by('product__category'),
        }
        result = render_to_string('basketapp/includes/inc_basket_list.html', context)

        data = {
            'result': result,
        }

        return JsonResponse(data)

@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# def basket_remove(request, pk):
#     content = {}
#     return render(request, 'basketapp/basket.html', content)
#
# def basket_remove(request, pk):
#     basket_item = Basket.objects.filter(pk=pk).first()
#     if basket_item:
#         basket_item.delete()
#
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))