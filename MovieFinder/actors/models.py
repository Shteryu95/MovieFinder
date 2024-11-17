from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from MovieFinder.movies.models import Movie


class Actor(models.Model):
    full_name = models.CharField(
        max_length=30,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    nationality = models.CharField(
        max_length=30,
    )

    movies = models.ManyToManyField(
        Movie,
        related_name='actor',
    )
