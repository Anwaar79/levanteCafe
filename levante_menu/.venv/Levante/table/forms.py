from django import forms
from .models import Table


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['table_name']
        widgets = {
            'table_name': forms.TextInput(attrs={'placeholder': 'example: Table 1'}),
        }
