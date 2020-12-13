from django import forms
from .models import Shoe, NewShoe


class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ('shoeModel', 'brand_name', 'price',
                  'color', 'size', 'shoeAvail')


class NewShoeForm(forms.ModelForm):
    class Meta:
        model = NewShoe
        fields = ('shoeModel', 'brand_name', 'price',
                  'color', 'releaseDate', 'shoeAvail')
