from django.db import models
from django.db.models import CASCADE

from MovieFinder.accounts.models import CustomUser
from MovieFinder.movies.models import Movie


class Rating(models.Model):
    RATE_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    user = models.ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name='user_rating'
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=CASCADE,
        related_name='movie_rating'
    )

    rate = models.SmallIntegerField(
        choices=RATE_CHOICES,
    )


class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=CASCADE,
        related_name='user_comment'
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=CASCADE,
        related_name='movie_comment'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
