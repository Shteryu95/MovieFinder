from django.test import TestCase

from MovieFinder.accounts.forms import ProfileEditForm


class TestProfileForm(TestCase):

    def setUp(self):
        self.valid_data = {
            'first_name': None,
            'last_name': None,
            'age': 120,
            'profile_photo': None,
        }

    def test__username_contains_symbols__returns_error(self):
        self.valid_data['age'] = 120
        form = ProfileEditForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
