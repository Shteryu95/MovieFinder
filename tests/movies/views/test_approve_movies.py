from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from MovieFinder.movies.models import Movie

UserModel = get_user_model()


class TestApprovePostView(TestCase):

    def setUp(self):
        self.user_credentials = {
            "username": "asdasd",
            "password": "12314532523",
        }
        self.user = UserModel.objects.create_user(
            **self.user_credentials
        )
        self.movie = Movie.objects.create(
            name="movie",
            released_date="1212-12-12",
            genre="Action",
            poster="https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
            resume="sadasdsad",
        )

    def test__approve_movie__redirects_to_catalogue(self):
        self.client.login(
            username=self.user_credentials['username'],
            password=self.user_credentials['password'],
        )

        response = self.client.get(
            reverse('approve', args=[self.movie.pk]),
            HTTP_REFERER=reverse('movie-catalogue')
        )

        self.movie.refresh_from_db()

        self.assertTrue(self.movie.approved)
        self.assertRedirects(response, reverse('movie-catalogue'))

