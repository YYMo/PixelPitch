# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_auto_20160711_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(max_length=40960, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=40960),
        ),
    ]
