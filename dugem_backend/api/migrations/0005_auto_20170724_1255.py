# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 12:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_eventlist_event_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlist',
            name='event_date_time',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
