from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from MovieFinder.actors.validators import NameValidator
from MovieFinder.movies.models import Movie


class Actor(models.Model):
    full_name = models.CharField(
        max_length=30,
        validators=[NameValidator()],
    )

    photo = models.URLField()

    age = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    country = models.CharField(
        max_length=30,
    )

    all_movies = models.ManyToManyField(
        to=Movie,
        related_name='movie_actors',
        blank=True,
    )

    def save(self, *args, **kwargs):
        names = self.full_name.split()

        self.full_name = ' '.join([name.capitalize() for name in names])

        super(Actor, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name






