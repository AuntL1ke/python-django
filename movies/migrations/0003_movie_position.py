# Generated by Django 5.1.4 on 2025-01-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='position',
            field=models.CharField(blank=True, choices=[('1', 'Movie'), ('2', 'Series')], max_length=255, null=True),
        ),
    ]