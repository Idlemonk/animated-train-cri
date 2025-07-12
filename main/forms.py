from django import forms
from .models import RecoveryRequest, Contact

class RecoveryRequestForm(forms.ModelForm):
        
        class Meta:
        model = RecoveryRequest
        fields = ['name', 'email', 'wallet_address', 'crypto_type', 'issue_description']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'}),
                'wallet_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Wallet Address'}),
                'crypto_type': forms.Select(attrs={'class': 'form-control'}),
                'issue_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the issue in detail'}),
        }
        labels = {
                'name': 'Full Name',
                'email': 'Email Address',
                'wallet_address': 'Wallet Address',
                'crypto_type': 'Cryptocurrency Type',
                'issue_description': 'Issue Description',
        }


class ContactForm(forms.ModelForm):
        class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'country', 'type_of_recovery', 'message', 'privacy_policy']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
                'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
                'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}),
                'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Country'}),
                'type_of_recovery': forms.Select(attrs={'class': 'form-control'}),
                'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
                'privacy_policy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }