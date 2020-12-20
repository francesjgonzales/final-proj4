from .forms import ShoeForm, NewShoeForm
from .models import Shoe, NewShoe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.


def index(request):
    shoes = Shoe.objects.all()
    newShoes = NewShoe.objects.all()
    return render(request, 'shoes/index.template.html', {
        'shoes': shoes,
        'newShoes': newShoes
    })


def main(request):
    shoes = Shoe.objects.all()
    newShoes = NewShoe.objects.all()
    return render(request, 'shoes/main.template.html', {
        'shoes': shoes,
        'newShoes': newShoes
    })


def view_shoe(request, shoe_id):
    view_shoes = get_object_or_404(Shoe, pk=shoe_id)
    return render(request, 'shoes/view_shoe.template.html', {
        'shoes': view_shoes,
    })


def view_newshoe(request):
    view_newshoes = Shoe.objects.all()
    return render(request, 'shoes/view_newshoe.template.html', {
        'newshoes': view_newshoes,
    })


@login_required
def create_shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"New Shoe {form.cleaned_data['shoeModel']} is created")
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
            messages.success(
                request, f"New Shoe {form.cleaned_data['shoeModel']} is created")
            return redirect(reverse(index))
    else:
        create_newShoe_form = NewShoeForm()
        return render(request, 'shoes/create_newshoe.template.html', {
            'form': create_newShoe_form
        })


def edit_shoe(request, shoe_id):
    shoe_update = get_object_or_404(Shoe, pk=shoe_id)

    if request.method == "POST":
        shoe_form = ShoeForm(request.POST, instance=shoe_update)
        if shoe_form.is_valid():
            shoe_form.save()
            messages.success(
                request, f"Shoe {shoe_form.cleaned_data['shoeModel']} is edited")
            return redirect(reverse(index))
        else:
            return render(request, 'shoes/edit_shoe.template.html', {
                'form': shoe_form
            })
    else:
        shoe_form = ShoeForm(instance=shoe_update)
        return render(request, 'shoes/edit_shoe.template.html', {
            'form': shoe_form
        })


def edit_newshoe(request, newShoe_id):
    newshoe_update = get_object_or_404(NewShoe, pk=newShoe_id)

    if request.method == "POST":
        new_shoe_form = NewShoeForm(request.POST, instance=newshoe_update)
        if new_shoe_form.is_valid():
            new_shoe_form.save()
            messages.success(
                request, f"Upcoming Shoe {form.cleaned_data['shoeModel']} is edited"
            )
            return redirect(reverse(index))
        else:
            return render(request, 'shoes/edit_newshoe.template.html', {
                'form': new_shoe_form
            })
    else:
        newshoe_form = NewShoeForm(instance=newshoe_update)
        return render(request, 'shoes/edit_newshoe.template.html', {
            'form': newshoe_form,
        })


def delete_shoe(request, shoe_id):
    shoe_to_delete = get_object_or_404(Shoe, pk=shoe_id)
    if request.method == 'POST':
        shoe_to_delete.delete()
        messages.error(request, f'Shoe is deleted')
        return redirect(index)
    else:
        return render(request, 'shoes/delete_shoe.template.html', {
            'shoe': shoe_to_delete
        })


def delete_newshoe(request, newShoe_id):
    newshoe_to_delete = get_object_or_404(NewShoe, pk=newShoe_id)
    if request.method == 'POST':
        newshoe_to_delete()
        return redirect(index)
    else:
        return render(request, 'shoes/delete_newshoe.template.html', {
            'newshoe': newshoe_to_delete
        })
