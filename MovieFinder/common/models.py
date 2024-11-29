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
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )

    text = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
