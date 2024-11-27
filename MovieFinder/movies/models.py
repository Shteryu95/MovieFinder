from django.db import models
from django.db.models import CASCADE, Avg

from MovieFinder.accounts.models import CustomUser
from MovieFinder.actors.models import Actor
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

    main_actors = models.ManyToManyField(
        Actor,
        related_name='starred_movie'
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

    class Meta:
        ordering = ['name', ]

    @property
    def average_rating(self):

        ratings = self.movie_rating.all()
        if ratings.exists():
            return round(ratings.aggregate(Avg('rating'))['rating__avg'], 1)
        return None
