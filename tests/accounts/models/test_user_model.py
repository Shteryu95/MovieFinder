from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class TestUserModel(TestCase):

    def test__valid__str__method(self):
        user = UserModel.objects.create_user(
            username='kiril',
            password='asdqwezxfc',
        )

        self.assertEqual(str(user), 'kiril')

    def test__valid_str_method__profile(self):
        user = UserModel.objects.create_user(
            username='gosho',
            password='asdqwezxfc',
        )

        user.profile.first_name = 'georgi'
        user.profile.last_name = 'kolev'

        self.assertEqual(str(user.profile), 'georgi kolev')