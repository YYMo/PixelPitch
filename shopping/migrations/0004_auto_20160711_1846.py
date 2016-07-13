# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_artist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(help_text=b'Please Paste in HTML marked text, for Example: <p> Hello </p>', max_length=4096, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(help_text=b'Please Paste in HTML marked text, for Example: <p> Hello </p>', max_length=4096),
        ),
    ]
