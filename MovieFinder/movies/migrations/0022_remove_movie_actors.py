# Generated by Django 5.1.3 on 2024-12-01 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_remove_movie_main_actors_movie_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
    ]
