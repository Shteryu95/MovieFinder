from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from MovieFinder.accounts.forms import CustomUserCreationForm, ProfileEditForm
from MovieFinder.accounts.models import Profile

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
    model = Profile
    template_name = 'profile-details.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile-edit.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.request.user.pk})


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'profile-delete.html'
    success_url = reverse_lazy('home')


