from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from plant.models import MyProfile
from django.contrib.auth.forms import PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forma', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': '', 'placeholder': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': '', 'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': '', 'placeholder': 'confirm password'}))
    status = forms.ChoiceField(choices=MyProfile.STATUS_CHOICES) 

    class Meta:
        model = User  
        fields = ('username', 'email', 'password1', 'password2', 'status')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.status = self.cleaned_data['status']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'forma', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'forma', 'placeholder': 'password'}))
        
    class Meta:
        model = User  
        fields = ['username', 'password']
        
class UserUpdateForm(forms.ModelForm):
    
    STATUS_CHOICES = [
        ('Seller', 'Salesman'),
        ('Buyer', 'Buyer'),
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
   
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
        widgets = {
            'username':forms.TextInput(attrs={'placeholder': 'username'},),
            'email':forms.EmailInput(attrs={'placeholder': 'email'},),
            'first_name':forms.TextInput(attrs={'placeholder': 'first_name'},),
            'last_name':forms.TextInput(attrs={'placeholder': 'last_name'},),
        }
        
    
    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        
        status = self.cleaned_data.get('status')
        profile, created = MyProfile.objects.get_or_create(user=user)
        profile.status = status
        profile.save()
        
        return user

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['placeholder'] = 'Current password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm password'