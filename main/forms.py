from django import forms
from .models import ContactMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput(attrs = {
        'class': 'from-control form-control-lg',
        'placeholder': 'Enter your email address',
        'autocomplete': 'email'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        