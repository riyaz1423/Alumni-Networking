from django import forms
from django.contrib.auth.models import User
from .models import Alumni

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'validate', 'placeholder': 'Enter Password'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Enter Username'}),
            'email': forms.EmailInput(attrs={'class': 'validate', 'placeholder': 'Enter Email'}),
        }

class AlumniProfileForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['email', 'password', 'batch', 'department', 'position', 'company', 'contact']
        widgets = {
            'batch': forms.NumberInput(attrs={'class': 'validate', 'placeholder': 'Enter Batch Year'}),
            'department': forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Enter Department'}),
            'position': forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Enter Position'}),
            'company': forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Enter Company'}),
            'contact': forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Enter Contact Number'}),
        }
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )