from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    
    SALESMAN = 'salesman'
    BUYER = 'buyer'
    
    STATUS = [
        (SALESMAN, SALESMAN),
        (BUYER, BUYER)
    ]
        
               
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forma', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': '', 'placeholder': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': '', 'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': '', 'placeholder': 'confirm password'}))
    status = forms.ChoiceField(choices=STATUS, initial=BUYER)
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forma', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': '', 'placeholder': 'password'}))
        
    class Meta:
        model = User  
        fields = ['username', 'password']
        
class UserUpdateForm(forms.ModelForm):
    
    # SALESMAN = 'salesman'
    # BUYER = 'buyer'
    # STATUS = [
    #     (SALESMAN, 'Salesman'),
    #     (BUYER, 'Buyer')
    # ]
    
    # status = forms.ChoiceField(choices=STATUS, initial=BUYER)
   
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
        widgets = {
            'username':forms.TextInput(attrs={'placeholder': 'username'},),
            'email':forms.EmailInput(attrs={'placeholder': 'email'},),
            'first_name':forms.TextInput(attrs={'placeholder': 'first_name'},),
            'last_name':forms.TextInput(attrs={'placeholder': 'last_name'},),
        }
