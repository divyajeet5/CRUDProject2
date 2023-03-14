from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class Registration(UserCreationForm):

    model = User
    email = forms.EmailField(required=True)

    # Below code does not work...

    fields = ['name', 'email', 'password1', 'password2']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'password1': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        'password2': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
    }
