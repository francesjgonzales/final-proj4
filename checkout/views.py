from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
import stripe
import json
from django.conf import settings
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from shoes.models import Shoe


# Create your views here.


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})

    line_items = []
    all_shoe_ids = []

    for shoe_id, cart_item in cart.items():
        shoe = get_object_or_404(Shoe, pk=shoe_id)

        # items in dictionary is prefix by stripes
        item = {
            "name": shoe.shoeModel,
            "amount": int(shoe.price * 100),
            "quantity": cart_item['qty'],
            "currency": "usd",

        }

        line_items.append(item)
        all_shoe_ids.append({
            'shoe_id': shoe.id,
            'qty': cart_item['qty']
        })

    current_site = Site.objects.get_current()

    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],  # take credit cards
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_shoe_ids": json.dumps(all_shoe_ids)
        },
        mode="payment",
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout/checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })


def checkout_success(request):
    return HttpResponse("Payment completed successfully")


def checkout_cancelled(request):
    return HttpResponse("Checkout cancelled")


@csrf_exempt
def payment_completed(request):
    print('request.body')
    return HttpResponse(status=200)
