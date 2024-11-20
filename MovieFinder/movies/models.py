from django.db import models
from django.db.models import CASCADE

from MovieFinder.accounts.models import CustomUser


class Movie(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('horror', 'Horror'),
        ('drama', 'Drama'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('biography', 'Biography'),
        ('anime', 'Anime'),
        ('musical', 'Musical'),
        ('mistery', 'Mistery'),
        ('crime', 'Crime'),
        ('adventure', 'Adventure'),
        ('documentary', 'Documentary'),
        ('sci-fi', 'Sci-Fi'),
        ('sport', 'Sport'),
        ('western', 'Western'),
    ]

    name = models.CharField(
        max_length=50
    )

    released_date = models.DateField()

    genre = models.CharField(
        choices=GENRE_CHOICES,
    )

    poster = models.URLField()

    awards = models.CharField(
        max_length=100,
    )

    resume = models.TextField(
        max_length=300,
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=CASCADE,
    )