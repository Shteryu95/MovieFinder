# Generated by Django 5.1.3 on 2024-12-02 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0023_movie_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['name'], 'permissions': [('approve_movies', 'Approve movies')]},
        ),
    ]