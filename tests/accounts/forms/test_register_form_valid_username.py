from django.test import TestCase

from MovieFinder.accounts.forms import CustomUserCreationForm


class TestRegisterForm(TestCase):

    def setUp(self):
        self.valid_data = {
            'username': 'fafdsadas',
            'password1': '123456789',
            'password2': '123456789',
        }

    def test__username_contains_symbols__returns_error(self):
        self.valid_data['username'] = 'asdsad___'
        form = CustomUserCreationForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test__password2_different_than_password1__returns_error(self):
        self.valid_data['password1'] = '123456789'
        self.valid_data['password2'] = 'asd123456'
        form = CustomUserCreationForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)


