from django.shortcuts import render, get_object_or_404, redirect, reverse
from shoes.models import Shoe

# Create your views here.


def add_to_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    cart = request.session.get('shopping_cart', {})

    if shoe_id not in cart:
        cart[shoe_id] = {
            'id': shoe_id,
            'shoeModel': shoe.shoeModel,
            'price': 99,
            'qty': 1
        }
    else:
        cart[shoe_id]['qty'] += 1

    request.session['shopping_cart'] = cart
    return redirect(reverse('view_cart'))


def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })
