# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('nick_name', models.CharField(max_length=64)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(default=b'M', max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')])),
                ('type', models.CharField(default=b'PHOTO', max_length=32, choices=[(b'PHOTO', b'Photographer'), (b'PAINTER', b'Painter')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=1024)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('avatar', models.ImageField(upload_to=b'')),
                ('creator', models.ForeignKey(to='shopping.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=1024)),
                ('creator', models.ForeignKey(to='shopping.Artist')),
                ('item', models.ForeignKey(to='shopping.Item')),
            ],
        ),
    ]
