from django.db import models
from django.db.models import CASCADE

from MovieFinder.accounts.models import CustomUser
from MovieFinder.movies.models import Movie


class Rating(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name='user_rating'
    )

    to_movie = models.ForeignKey(
        to=Movie,
        on_delete=CASCADE,
        related_name='movie_rating'
    )

    rating = models.SmallIntegerField(
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ('user', 'to_movie')


class Comment(models.Model):
    text = models.TextField(
        max_length=300,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    to_movie = models.ForeignKey(
        to=Movie,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
    )

