from django import forms
from .models import Product


STYLES = 'w-full py-3 px-6 rounded-xl bg-white hover:border-2 border-gray-700'

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'categories', 'description', 'price', 'image', 'is_available', 'stock_quantity')
        widgets = {
            'categories': forms.SelectMultiple(attrs={
                'class': STYLES,
                'size': 5
            }),
            'name': forms.TextInput(attrs={
                'class': STYLES
            }),
            'description': forms.Textarea(attrs={
                'class': STYLES
            }),
            'price': forms.NumberInput(attrs={
                'class': STYLES
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 rounded accent-green-600'
            }),
            'stock_quantity': forms.NumberInput(attrs={
                'class': STYLES
            }),
            'image': forms.FileInput(attrs={
                'class': STYLES
            })
        }

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'categories', 'description', 'price', 'image', 'is_available', 'stock_quantity')
        widgets = {
            'categories': forms.SelectMultiple(attrs={
                'class': STYLES,
                'size': 5
            }),
            'name': forms.TextInput(attrs={
                'class': STYLES
            }),
            'description': forms.Textarea(attrs={
                'class': STYLES
            }),
            'price': forms.NumberInput(attrs={
                'class': STYLES
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 rounded accent-green-600'
            }),
            'stock_quantity': forms.NumberInput(attrs={
                'class': STYLES
            }),
            'image': forms.FileInput(attrs={
                'class': STYLES
            })
        }