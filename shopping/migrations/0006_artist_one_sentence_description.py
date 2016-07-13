# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20160711_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='one_sentence_description',
            field=models.TextField(max_length=1024, blank=True),
        ),
    ]
