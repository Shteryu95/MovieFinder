# Generated by Django 5.1.3 on 2024-12-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0007_actor_all_movies'),
        ('movies', '0024_alter_movie_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='all_movies',
            field=models.ManyToManyField(blank=True, null=True, related_name='movie_actors', to='movies.movie'),
        ),
    ]
