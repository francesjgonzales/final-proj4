def cart_content(request):
    cart = request.session.get('shopping_cart', {})
    return {
        'shopping_cart': cart,
        'number_of_items': len(cart)
    }
