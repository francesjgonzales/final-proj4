from django import forms
from .models import Shoe, NewShoe


class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ('shoeModel', 'shoeBrand', 'price',
                  'color', 'size', 'shoeAvail')


class NewShoeForm(forms.ModelForm):
    class Meta:
        model = NewShoe
        fields = ('shoeModel', 'shoeBrand', 'price',
                  'color', 'releaseDate', 'shoeAvail')
