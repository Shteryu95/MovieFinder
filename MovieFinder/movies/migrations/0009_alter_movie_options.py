# Generated by Django 5.1.3 on 2024-11-27 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_movie_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['name']},
        ),
    ]
