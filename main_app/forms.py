
from django import forms
from .models import Accessory


class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory

        fields = [
            "type", "color", "description", "img_url"
        ]
