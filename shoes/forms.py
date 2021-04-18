from django import forms
from .models import Shoe, Brand
from cloudinary.forms import CloudinaryJsFileField


class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ('__all__')
    image = CloudinaryJsFileField()


class SearchForm(forms.Form):
    shoeModel = forms.CharField(
        required=False, max_length=255, label='Shoe Model',
        widget=forms.TextInput(attrs={'placeholder': 'Search'})
    )
    brand_name = forms.ModelChoiceField(
        queryset=Brand.objects.all(), required=False)
