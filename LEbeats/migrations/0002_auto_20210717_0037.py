# Generated by Django 3.2.5 on 2021-07-17 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LEbeats', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='author',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='published_date',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='album',
            name='created_date',
        ),
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
