
from django import forms
from .models import Accessory
# from .models import Review

class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory

        fields = [
            "type", "color", "description", "img_url", "price"
        ]
        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review

#         fields = [
#             "text"
#         ]