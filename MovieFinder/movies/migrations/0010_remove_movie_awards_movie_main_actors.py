# Generated by Django 5.1.3 on 2024-11-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_remove_actor_movies'),
        ('movies', '0009_alter_movie_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='awards',
        ),
        migrations.AddField(
            model_name='movie',
            name='main_actors',
            field=models.ManyToManyField(related_name='starred_movie', to='actors.actor'),
        ),
    ]
