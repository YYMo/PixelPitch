# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 01:16
from __future__ import unicode_literals

from django.db import migrations, models
import shopping.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0010_artist_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='item',
        ),
        migrations.AddField(
            model_name='photo',
            name='upload',
            field=models.FileField(default=b' ', upload_to=shopping.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.TextField(max_length=128),
        ),
    ]