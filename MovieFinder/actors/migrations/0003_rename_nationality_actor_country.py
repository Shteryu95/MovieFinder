# Generated by Django 5.1.3 on 2024-11-30 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_remove_actor_movies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='nationality',
            new_name='country',
        ),
    ]