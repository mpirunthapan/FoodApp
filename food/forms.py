from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']