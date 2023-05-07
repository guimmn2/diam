from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Password", max_length=100, widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Confirm password", max_length=100, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if password != confirm_password:
            self._errors['password'] = self.error_class(['Passwords do not match'])

        if User.objects.filter(username=username).exists():
            self._errors['username'] = self.error_class([username + ' already exists'])

        if User.objects.filter(email=email).exists():
            self._errors['email'] = self.error_class([email + ' is registered in another account'])

        if len(username) < 5:
            self._errors['username'] = self.error_class(['Minimum 5 characters required'])

        if len(password) < 8:
            self._errors['password'] = self.error_class(['Minimum 8 characters required'])

        return cleaned_data
