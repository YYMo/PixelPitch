# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='avatar',
            field=models.URLField(max_length=256),
        ),
        migrations.AlterField(
            model_name='artist',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='first_name',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=64, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='avatar',
            field=models.URLField(max_length=256),
        ),
    ]
