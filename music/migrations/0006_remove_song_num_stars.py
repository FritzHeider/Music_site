# Generated by Django 3.0.4 on 2020-04-22 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20200421_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='num_stars',
        ),
    ]
