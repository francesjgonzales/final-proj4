from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from shoes.models import Shoe


def add_to_cart(request, shoe_id):
    shoe_cart = request.session.get('shopping_cart', {})

    if shoe_id not in shoe_cart:
        shoe = get_object_or_404(Shoe, pk=shoe_id)

        shoe_cart[shoe_id] = {
            'shoe_id': shoe_id,
            'shoeModel': shoe.shoeModel,
            'price': "{:.2g}".format(shoe.price/100),
            'qty': 1
        }
        request.session['shopping_cart'] = shoe_cart
        messages.success(request, f"{shoe.shoeModel} is added in the cart")
        return redirect(reverse('main_shoe'))

    else:
        shoe_cart[shoe_id]['qty'] += 1
        # shoe_cart[shoe_id]['price'] = round(
        #     int(shoe_cart[shoe_id]['qty']) *
        #     float(shoe_cart[shoe_id]['price']), 2)
        request.session['shopping_cart'] = shoe_cart
        return redirect(reverse('view_cart'))


def view_cart(request):
    shoe_cart = request.session.get('shopping_cart', {})

    return render(request, 'cart/view_cart.template.html', {
        'shopping_cart': shoe_cart
    })


def remove_from_cart(request, shoe_id):
    shoe_cart = request.session.get('shopping_cart', {})
    if shoe_id in shoe_cart:
        del shoe_cart[shoe_id]
        request.session['shopping_cart'] = shoe_cart
        messages.success(request, "Shoes is removed from cart successfully!")
    return redirect(reverse('remove_from_cart'))


def edit_quantity(request, shoe_id):
    shoe_cart = request.sessions.get('shopping_cart', {})

    if shoe_id in shoe_cart:
        shoe_cart[shoe_id]['qty'] = request.POST['qty']
        request.session['shopping_cart'] = shoe_cart
        messages.success(request, 'Quantity is updated')
    return redirect(reverse('view_cart'))
