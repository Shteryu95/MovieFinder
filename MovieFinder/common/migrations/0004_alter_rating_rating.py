# Generated by Django 5.1.3 on 2024-11-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_rating_unique_together_rating_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]