# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_eventlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlist',
            name='event_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='eventlist',
            name='venue_id',
            field=models.IntegerField(),
        ),
    ]
