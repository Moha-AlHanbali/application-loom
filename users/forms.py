from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Applicant


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Applicant
        fields = ('username', 'email', 'password1', 'password2')

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
