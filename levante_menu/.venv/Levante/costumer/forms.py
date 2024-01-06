from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-2', 'placeholder': 'Your name..'}),
            'email': forms.EmailInput(attrs={'class': 'col-2', 'placeholder': 'johndoe@example.com', 'style': 'background: none; border: none; border-bottom: 2px solid #a7772b; width: 98%; color:#a7772b;'}),
            'message': forms.Textarea(attrs={'class': 'col-2', 'placeholder': 'Share your ideas..', 'style': 'height:100px; width: 98%;'}),
        }