from django import forms
from .models import Order
from django.forms import ModelForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['table_choice', 'items']
        widgets = {
           'table_choice': forms.Select(attrs={'class': 'tableop'}),
           'items': forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox'}),
        }


    def __init__(self, *args, **kwargs):
     menu_items = kwargs.pop('menu_items', None)
     super().__init__(*args, **kwargs)
     if menu_items is not None:
        self.fields['items'].queryset = menu_items

    def label_from_instance(self, obj):
        return str(obj.table_id) 