from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    """Form that allows user to registrate"""
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'fullname', 'password')

    def clean_password_confirmation(self):
        """Checking if both passwords are the same"""
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            raise ValidationError("Password don't match")

        return password_confirmation

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        user.is_active = True

        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    """Form that allows user to login"""
    username = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={
            'name': 'username',
            'placeholder': 'Email'
        })
    )

    class Meta:
        fields = ('username', 'password')

    error_messages = {
        "invalid_login": "Please enter a correct email and password."
    }
