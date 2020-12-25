from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from shoes.models import Shoe

# Create your views here.


def add_to_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)

    cart = request.session.get('shopping_cart', {})

    if shoe_id not in cart:
        cart[shoe_id] = {
            'id': shoe_id,
            'shoeModel': shoe.shoeModel,
            'price': str(shoe.price),
            'total_price': float(shoe.price),
            'qty': 1,
            'shoe_size': shoe.shoe_size,
            'image': str(shoe.image)
        }
    else:
        cart[shoe_id]['qty'] += 1
        cart[shoe_id]['total_price'] = round(
            int(cart[shoe_id]['qty']) * float(cart[shoe_id]['price']), 2)

    request.session['shopping_cart'] = cart
    messages.success(request, 'Item is added to your cart')
    return redirect(reverse('view_cart'))


def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    total_price = 0.00
    grand_total_price = 0.00
    for key, i in cart.items():
        total_price == i['total_price']
        grand_total_price += i['total_price']

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart,
        'grand_total_price': round(grand_total_price, 2)
    })


def remove_from_cart(request, shoe_id):
    cart = request.session.get('shopping_cart', {})

    if shoe_id in cart:
        del cart[shoe_id]

        request.session['shopping_cart'] = cart
        messages.info(request, 'Item is removed from your cart')

    return redirect(reverse('view_cart'))


