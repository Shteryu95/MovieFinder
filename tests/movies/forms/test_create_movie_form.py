from django.test import TestCase

from MovieFinder.movies.forms import MovieBaseForm


class TestMovieBaseForm(TestCase):

    def setUp(self):
        self.valid_data = {
            'name': 'aaaaaa',
            'released_date': '12/12/1999',
            'genre': 'Action',
            'poster': 'https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg',
            'resume': 'dsfdsf',
        }

    def test__form_is_valid__true(self):
        form = MovieBaseForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test__empty_name__returns_error(self):
        self.valid_data['name'] = ''
        form = MovieBaseForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

