# Generated by Django 5.1.3 on 2024-12-07 08:55

import MovieFinder.actors.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0009_alter_actor_all_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='full_name',
            field=models.CharField(max_length=30, validators=[MovieFinder.actors.validators.NameValidator()]),
        ),
    ]