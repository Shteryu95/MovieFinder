# Generated by Django 5.1.3 on 2024-11-30 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_movie_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='resume',
            field=models.TextField(max_length=300),
        ),
    ]
