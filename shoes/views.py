from django.shortcuts import render
from .models import Shoe, NewShoe
from .forms import ShoeForm

# Create your views here.


def index(request):
    shoes = Shoe.objects.all()
    newShoes = NewShoe.objects.all()
    return render(request, 'shoes/index.template.html', {
        'shoes': shoes,
        'newShoes': newShoes
    })


def create_shoe(request):
    create_shoe_form = ShoeForm()
    return render(request, 'shoes/create_shoe.template.html', {
        'form': create_shoe_form
    })
