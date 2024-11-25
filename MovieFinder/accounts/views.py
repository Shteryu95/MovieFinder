from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from MovieFinder.accounts.forms import CustomUserCreationForm

UserModel = get_user_model()


class UserLoginView(LoginView):
    template_name = 'login-page.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username',
        })
        form.fields['password'].widget.attrs.update({
            'placeholder': 'Enter your password',
        })
        return form


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register-page.html'


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'profile-details.html'
