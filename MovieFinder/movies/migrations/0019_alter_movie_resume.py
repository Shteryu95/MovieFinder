# Generated by Django 5.1.3 on 2024-11-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_alter_movie_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='resume',
            field=models.CharField(max_length=300),
        ),
    ]
