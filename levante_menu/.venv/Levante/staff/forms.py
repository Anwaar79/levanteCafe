from django import forms
from .models import User


class StaffLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['staff_name', 'staff_password']
        widgets = {
            'staff_name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'staff_password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }


class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['staff_name', 'staff_password']
        widgets = {
            'staff_name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'staff_password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }

