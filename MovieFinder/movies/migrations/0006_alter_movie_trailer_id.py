# Generated by Django 5.1.3 on 2024-11-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movie_trailer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer_id',
            field=models.CharField(blank=True, null=True),
        ),
    ]