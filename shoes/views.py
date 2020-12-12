from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Shoe, NewShoe
from .forms import ShoeForm, NewShoeForm

# Create your views here.


def index(request):
    shoes = Shoe.objects.all()
    newShoes = NewShoe.objects.all()
    return render(request, 'shoes/index.template.html', {
        'shoes': shoes,
        'newShoes': newShoes
    })


def create_shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(index))
    else:
        create_shoe_form = ShoeForm()
        return render(request, 'shoes/create_shoe.template.html', {
            'form': create_shoe_form
        })


def create_newshoe(request):
    if request.method == "POST":
        form = NewShoeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(index))
    else:
        create_newShoe_form = NewShoeForm()
        return render(request, 'shoes/create_newshoe.template.html', {
            'form': create_newShoe_form
        })


def edit_shoe(request, shoe_id):
    shoe_update = get_object_or_404(Shoe, pk=shoe_id)

    if request.method == "POST":
        form = ShoeForm(request.POST, instance=shoe_update)
        if form.is_valid():
            form.save()
            return redirect(reverse(index))
    else:
        shoe_form = ShoeForm(instance=shoe_update)
        return render(request, 'shoes/edit_shoe.template.html', {
            'form': shoe_form,
            'shoe': shoe_update
        })


def edit_newshoe(request, newShoe_id):
    newshoe_update = get_object_or_404(Shoe, pk=newShoe_id)

    if request.method == "POST":
        form = NewShoeForm(request.POST, instance=newshoe_update)
        if form.is_valid():
            form.save()
            return redirect(reverse(index))
    else:
        newshoe_form = NewShoeForm(instance=newshoe_update)
        return render(request, 'shoes/edit_newshoe.template.html', {
            'form': newshoe_form,
            'newshoe': newshoe_update
        })
