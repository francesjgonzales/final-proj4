from .forms import ShoeForm, SearchForm
from .models import Shoe, Brand
from reviews.forms import ReviewForm
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.


# Admin welcome page
@login_required
def index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.template.html', {
        'shoes': shoes
    })


# Consumer welcome page
def home_consumer(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/home_consumer.template.html', {
        'shoes': shoes
    })


# Admin product page
def home(request):
    shoes = Shoe.objects.all()

    if request.GET:
        queries = ~Q(pk__in=[])

        if 'brand_name' in request.GET and request.GET['brand_name']:
            brand_name = request.GET['brand_name']
            queries = queries & Q(brand_name__in=brand_name)

        if 'shoeModel' in request.GET and request.GET['shoeModel']:
            shoeModel = request.GET['shoeModel']
            queries = queries & Q(shoeModel__icontains=shoeModel)

        shoes = shoes.filter(queries)

    brand_name = Brand.objects.all()
    search_form = SearchForm(request.GET)

    return render(request, 'shoes/home.template.html', {
        'shoes': shoes,
        'search_form': search_form
    })


# Consumer product page
def main(request):
    shoes = Shoe.objects.all()

    if request.GET:
        queries = ~Q(pk__in=[])

        if 'brand_name' in request.GET and request.GET['brand_name']:
            brand_name = request.GET['brand_name']
            queries = queries & Q(brand_name__in=brand_name)

        if 'shoeModel' in request.GET and request.GET['shoeModel']:
            shoeModel = request.GET['shoeModel']
            queries = queries & Q(shoeModel__icontains=shoeModel)

        shoes = shoes.filter(queries)

    brand_name = Brand.objects.all()
    search_form = SearchForm(request.GET)

    return render(request, 'shoes/main.template.html', {
        'shoes': shoes,
        'search_form': search_form
    })


# Admin - each product information
@login_required
def shoe_info(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    shoes = Shoe.objects.all()
    review_form = ReviewForm()
    return render(request, 'shoes/shoe_info.template.html', {
        'shoe': shoe,
        'shoes': shoes,
        'form': review_form
    })


# Consumer - each product information
def consumer_shoe_info(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    shoes = Shoe.objects.all()
    review_form = ReviewForm()
    return render(request, 'shoes/consumer_shoe_info.template.html', {
        'shoe': shoe,
        'shoes': shoes,
        'form': review_form
    })


# Admin shoe form
def create_shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"{form.cleaned_data['shoeModel']} is created")
        return redirect(reverse(home))
    else:
        create_shoe_form = ShoeForm()
        return render(request, 'shoes/create_shoe.template.html', {
            'form': create_shoe_form
        })


# Admin edit shoe form
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


# Admin delete shoe page
def delete_shoe(request, shoe_id):
    shoe_to_delete = get_object_or_404(Shoe, pk=shoe_id)
    if request.method == 'POST':
        shoe_to_delete.delete()
        messages.error(
            request, f"Shoe is deleted")
        return redirect(home)
    else:
        return render(request, 'shoes/delete_shoe.template.html', {
            'shoe': shoe_to_delete
        })


# Admin/Consumer shoe page
def contact(request):
    return render(request, 'shoes/contact.template.html')
