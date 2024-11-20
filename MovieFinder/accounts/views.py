from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from MovieFinder.accounts.forms import CustomUserCreationForm

UserModel = get_user_model()


class UserLoginView(LoginView):
    template_name = 'login-page.html'


class UserRegisterView(CreateView):
    model = UserModel
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register-page.html'
