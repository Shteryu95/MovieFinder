from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from MovieFinder.movies.models import Movie

UserModel = get_user_model()


class TestMovieDelete(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='pesho',
            password='12345qwerty'
        )

        self.user.is_staff = True

        self.movie = Movie.objects.create(
            name="movie",
            released_date="1212-12-12",
            genre="Action",
            poster="https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            resume="sadasdsad",
        )

        self.client.login(
            username='pesho',
            password='12345qwerty'
        )

    def test_movie_delete__from_staff_user__expect_in_success(self):
        self.assertTrue(Movie.objects.filter(pk=self.movie.pk).exists())

        response = self.client.post(
            reverse('movie-delete', kwargs={'pk': self.movie.pk})
        )

        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())
        self.assertRedirects(response, reverse('movie-catalogue'))

