from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
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
        return super().form_valid(form=form)
    # def get(self, request):
    #     form = forms.LoginForm(initial={"email": "blessambel1@gmail.com"})
    #     return render(request, template_name="users/login.html", context={"form": form})
    #
    # def post(self, request):
    #     form = forms.LoginForm(request.POST)
    #     if form.is_valid():
    #         email = form.cleaned_data.get("email")
    #         password = form.cleaned_data.get("password")
    #         user = authenticate(request=request, username=email, password=password)
    #         if user is not None:
    #             login(request=request, user=user)
    #             return redirect(reverse("core:home"))
    #     return render(request, template_name="users/login.html", context={"form": form})


def log_out(request):
    logout(request=request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    template_name = "users/signup.html"

