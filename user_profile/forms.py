from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'forms'})
        }

class LoginForm(AuthenticationForm):...
    # class Meta:
    #     model = User  
    #     fields = ['username', 'password']

    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forms'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'forms'}))