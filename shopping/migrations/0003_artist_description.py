# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20160708_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='description',
            field=models.TextField(max_length=1024, blank=True),
        ),
    ]
