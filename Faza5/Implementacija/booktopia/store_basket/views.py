from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView

from store.models import Product
from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    context = {
        'basket': basket
    }
    return render(request, 'store/basket/summary.html', context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket(request):
    return {'basket': Basket(request)}


# payment views
def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'account/payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'account/payment/error.html'


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    # stripe.api_key = ''
    # intent = stripe.PaymentIntent.create(
    #     amount=total,
    #     currency='gbp',
    #     metadata={'userid': request.user.id}
    # )
    context = {
        'amount': total,
        'currency': '$',
        'metadata': {'userid': request.user.id},
    }

    # return render(request, 'payment/home.html', {'client_secret': intent.client_secret})
    return render(request, 'account/payment/home.html', context)
