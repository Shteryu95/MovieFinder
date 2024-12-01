from django.db import models
from django.db.models import Avg
from django.urls import reverse_lazy

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

    resume = models.CharField(
        max_length=300,
    )

    trailer_id = models.CharField(
        null=True,
        blank=True,
    )

    user = models.CharField(
        max_length=100,
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

    @property
    def average_rating(self):

        ratings = self.movie_rating.all()
        if ratings.exists():
            return round(ratings.aggregate(Avg('rating'))['rating__avg'], 1)
        return None
