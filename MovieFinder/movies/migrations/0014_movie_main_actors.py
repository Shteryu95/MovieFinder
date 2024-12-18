# Generated by Django 5.1.3 on 2024-11-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_remove_actor_movies'),
        ('movies', '0013_alter_movie_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='main_actors',
            field=models.ManyToManyField(related_name='all_movies', to='actors.actor'),
        ),
    ]
