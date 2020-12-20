from django import forms
from .models import Shoe
from cloudinary.forms import CloudinaryJsFileField


class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ('__all__')
    image = CloudinaryJsFileField()
