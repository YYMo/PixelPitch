# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_auto_20160728_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='avatar',
            field=models.CharField(default=b'', max_length=256),
        ),
    ]
