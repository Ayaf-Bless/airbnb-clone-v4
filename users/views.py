import hashlib
import os

import requests
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import FormView

from . import forms, models


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


def github_login(request):
    client_id = os.environ.get('GITHUB_CLIENT_ID')
    redirect_url = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_url}&scope=read:user")


class GithubException(Exception):
    pass


def github_callback(request):
    try:
        code = request.GET.get("code", None)
        client_id = os.environ.get('GITHUB_CLIENT_ID')
        client_secret = os.environ.get('GITHUB_SECRET')

        if code:
            result = requests.post(
                f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                headers={"Accept": "application/json"})
            result_json = result.json()
            error = result_json.get("error", None)
            if error:
                raise GithubException()
            else:
                access_token = result_json.get("access_token")
                profile_request = requests.get("https://api.github.com/user",
                                               headers={"Authorization": f"token {access_token}",
                                                        "Accept": "application/json"})
                profile_json = profile_request.json()
                username = profile_json.get("login", None)
                if username:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    bio = profile_json.get("bio")
                    try:
                        user = models.User.objects.get(email=email)
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise GithubException()
                    except models.User.DoesNotExist:
                        user = models.User.objects.create(username=email,
                                                          first_name=name,
                                                          bio=bio,
                                                          email=email,
                                                          login_method=models.User.LOGIN_GITHUB)
                        user.set_unusable_password()
                        user.save()
                    login(request, user)
                    return redirect(reverse("core:home"))
                    # if user:
                    #     return redirect(reverse("users:login"))
                    # else:
                    #     user = models.User.objects.create(username=email, first_name=name, bio=bio, email=email)
                    #     login(request, user)
                    #     return redirect(reverse("core:home"))

                else:
                    raise GithubException()
        else:
            raise GithubException()
    except GithubException:
        return redirect(reverse("users:login"))


def kakao_login(request):
    rest_api_key = os.environ.get("KAKAO_API_KEY")
    redirect_url = "http://127.0.0.1:8000/users/login/kakao/callback"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={redirect_url}&response_type=code")


class KakaoException(Exception):
    pass


def kakao_callback(request):
    try:
        code = request.GET.get("code")
        client_id = os.environ.get("KAKAO_API_KEY")
        token_request = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}")
    except KakaoException:
        return redirect(reverse("users:login"))
