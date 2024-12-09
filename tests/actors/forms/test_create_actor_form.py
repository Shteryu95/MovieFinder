from django.test import TestCase

from MovieFinder.actors.forms import ActorBaseForm


class TestActorBaseForm(TestCase):

    def setUp(self):
        self.valid_data = {
            'full_name': 'dwayne johnson',
            'photo': 'https://israeled.org/wp-content/uploads/2018/04/gal-gadot.jpg',
            'age': '22',
            'country': 'USA',
        }

    def test__form_is_valid__true(self):
        form = ActorBaseForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test__full_name_not_only_letters__returns_error(self):
        self.valid_data['full_name'] = '13213231'
        form = ActorBaseForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)

    def test__full_name_with_one_word__returns_error(self):
        self.valid_data['full_name'] = 'racho'
        form = ActorBaseForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)

    def test__actor_create_full_name_validator_for_letters__error_message(self):
        self.valid_data['full_name'] = '1234'
        form = ActorBaseForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(["The full name of the actor must contain only letters and spaces!"], form["full_name"].errors)

    def test__actor_create_full_name_with_one_word__error_message(self):
        self.valid_data['full_name'] = 'dsfsdf'
        form = ActorBaseForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(["Full name must consist of more than one name."], form["full_name"].errors)

