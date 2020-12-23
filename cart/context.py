
def cart_contents(request):
    shoe_cart = request.session.get('shopping_cart', {})
    return {
        'shopping_cart': shoe_cart,
        'number_of_items': len(shoe_cart)
    }