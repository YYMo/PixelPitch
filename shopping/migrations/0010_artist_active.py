# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0009_item_buy_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]