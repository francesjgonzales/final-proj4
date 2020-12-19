from django import forms
from .models import Shoe, NewShoe
from cloudinary.forms import CloudinaryJsFileField


class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ('__all__')
    image = CloudinaryJsFileField()


class NewShoeForm(forms.ModelForm):
    class Meta:
        model = NewShoe
        fields = ('shoeModel', 'brand_name', 'price',
                  'color', 'releaseDate', 'shoeAvail')
