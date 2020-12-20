from .forms import ShoeForm
from .models import Shoe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.


def index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.template.html', {
        'shoes': shoes,
    })


def main(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/main.template.html', {
        'shoes': shoes,
    })


def shoe_info(request, shoe_id):
    shoe_info = get_object_or_404(Shoe, pk=shoe_id)
    return render(request, 'shoes/shoe_info.template.html', {
        'shoes': shoe_info
    })


@login_required
def create_shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"{form.cleaned_data['shoeModel']} is created")
            return redirect(reverse(index))
    else:
        create_shoe_form = ShoeForm()
        return render(request, 'shoes/create_shoe.template.html', {
            'form': create_shoe_form
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
