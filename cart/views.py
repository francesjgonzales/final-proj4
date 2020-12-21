from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from shoes.models import Shoe

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from shoes.models import Shoe


def add_to_cart(request, shoe_id):
    cart = request.session.get('shopping_cart', {})
    if shoe_id not in cart:
        shoe = get_object_or_404(Shoe, pk=shoe_id)
        cart[shoe_id] = {
            'id': shoe_id,
            'title': shoe.title,
            'cost': 99,
            'qty': 1
        }
        request.session['shopping_cart'] = cart

        messages.success(request, "Its added to your cart!")
        return redirect(reverse('book.views.index'))
    else:
        cart[shoe_id]['qty'] += 1
        request.session['shopping_cart'] = cart
        return redirect(reverse('shoes.views.index'))


def view_cart(request):
    cart = request.session.get('shopping_cart', {})

    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart': cart
    })


def remove_from_cart(request, shoe_id):
    cart = request.session.get('shopping_cart', {})
    if shoe_id in cart:
        del cart[shoe_id]
        request.session['shopping_cart'] = cart
        messages.success(request, "Item removed from cart successfully!")
    return redirect(reverse('view_shoes_route')
