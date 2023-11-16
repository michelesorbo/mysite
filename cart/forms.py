from django import forms
from shop.models import Product


class CartAddProductForm(forms.Form):
    PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 20)]
    
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
