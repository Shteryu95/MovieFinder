# Generated by Django 5.1.3 on 2024-12-01 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0003_rename_nationality_actor_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
