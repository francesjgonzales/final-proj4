from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from shoes.models import Shoe


def add_to_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    cart = request.session.get('shopping_cart', {})

    if shoe_id not in cart:
        cart[shoe_id] = {
            'shoe_id': shoe_id,
            'shoeModel': shoe.shoeModel,
            'price': "{:.2g}".format(shoe.price/100),
            'qty': 1
        }
    else:
        cart[shoe_id]['qty'] += 1

    request.session['shopping_cart'] = cart
    messages.success(request, f"{shoe.shoeModel} is added in the cart")
    return redirect(reverse('main_shoe'))


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
        messages.success(request, "Shoes is removed from cart")
        return redirect(reverse('main_shoe'))


def edit_quantity(request, shoe_id):
    cart = request.sessions.get('shopping_cart', {})

    if shoe_id in cart:
        cart[shoe_id]['qty'] = request.POST['qty']
        request.session['shopping_cart'] = cart
        messages.success(request, 'Quantity is updated')
    return redirect(reverse('view_cart'))
