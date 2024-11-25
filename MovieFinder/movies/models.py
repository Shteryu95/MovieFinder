from django.db import models
from django.db.models import CASCADE

from MovieFinder.accounts.models import CustomUser
from MovieFinder.movies.choices import GenreChoices


class Movie(models.Model):

    name = models.CharField(
        max_length=50
    )

    released_date = models.DateField()

    genre = models.CharField(
        choices=GenreChoices,
    )

    poster = models.URLField()

    awards = models.CharField(
        max_length=100,
    )

    resume = models.TextField(
        max_length=300,
    )

    trailer_id = models.CharField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=CASCADE,
    )