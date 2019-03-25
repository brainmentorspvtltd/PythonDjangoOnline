from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=100)
    email = forms.EmailField(label="Enter your email", max_length=100)