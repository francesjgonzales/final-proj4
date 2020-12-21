from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shoes.models import Shoe

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.template.html', {
        'reviews': reviews
    })


@login_required
def write_review(request, shoe_id):
    shoe = get_object_or_404(Shoe, pk=shoe_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.shoe = shoe
            review.save()
            messages.success(request, "Your review is added")
            return redirect(reverse(index))
    else:
        form = ReviewForm()
        return render(request, 'reviews/write_review.template.html', {
            'form': form,
            'shoe': shoe
        })
