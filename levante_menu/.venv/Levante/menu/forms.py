from django import forms
from django.forms import ModelForm
from .models import Item

class MenuForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'Cal', 'price', 'image', 'Food_Item_Type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dish title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'Cal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CAL'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'Food_Item_Type': forms.Select(attrs={'class': 'form-control'})
        }