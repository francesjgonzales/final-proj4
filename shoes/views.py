from django.shortcuts import render, HttpResponse
from .models import Shoe, NewShoe

# Create your views here.


def index(request):
    shoes = Shoe.objects.all()
    newShoes = NewShoe.objects.all()
    return render(request, 'shoes/index.template.html', {
        'shoes': shoes,
        'newShoes': newShoes
    })
