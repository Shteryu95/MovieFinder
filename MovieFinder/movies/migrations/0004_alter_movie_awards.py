# Generated by Django 5.1.3 on 2024-11-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='awards',
            field=models.CharField(max_length=100),
        ),
    ]