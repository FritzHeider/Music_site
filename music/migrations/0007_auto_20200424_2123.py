# Generated by Django 3.0.4 on 2020-04-24 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_remove_song_num_stars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='artist',
            new_name='band',
        ),
    ]