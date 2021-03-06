from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password",
                    forms.ValidationError("Check your credential and try again"),
                )
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    # def save(self):
    #     first_name = self.cleaned_data.get("first_name")
    #     last_name = self.cleaned_data.get("last_name")
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")

    #     user = models.User.objects.create_user(
    #         username=email, email=email, password=password
    #     )
    #     user.first_name = first_name
    #     user.last_name = last_name
    #     user.save()
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get("email")
        user.set_password(self.cleaned_data.get("password"))
        user.save()
