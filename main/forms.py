from django import forms
from .models import Bungalov, BungalovImage

class BungalovForm(forms.ModelForm):
    class Meta:
        model = Bungalov
        fields = ['name', 'description', 'price']

class BungalovImageForm(forms.ModelForm):
    class Meta:
        model = BungalovImage
        fields = ['image']
