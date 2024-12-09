from django.db import models

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

    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Movie, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name', ]
        permissions = [
            ('approve_movies', 'Approve movies'),
        ]

    def __str__(self):
        return self.name

    @property
    def average_rating(self):
        ratings = self.movie_rating.all()

        if ratings.exists():
            return sum(r.rating for r in ratings) / len(ratings)
        return None


