# Generated by Django 5.1.3 on 2024-12-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0004_actor_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='photo',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]