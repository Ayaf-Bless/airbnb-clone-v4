from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
import hashlib
from . import models

from . import forms


# Create your views here.
class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request=self.request, username=email, password=password)
        if user is not None:
            login(request=self.request, user=user)
        return super().form_valid(form)


def log_out(request):
    logout(request=request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    template_name = "users/signup.html"

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request=self.request, username=email, password=password)
        if user is not None:
            login(request=self.request, user=user)
            user.verify_email()
        return super().form_valid(form)


def complete_email_verification(request, token):
    hashed_token = hashlib.sha224(b"{token}").hexdigest()
    try:
        user = models.User.objects.get(email_token=hashed_token)
        user.email_verified = True
        user.email_token = ""
        user.save()
    except models.User.DoesNotExist:
        pass
    return redirect(reverse("core:home"))
