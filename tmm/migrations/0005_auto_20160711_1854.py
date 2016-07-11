# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tmm', '0004_auto_20160710_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 11, 18, 54, 21, 623496)),
        ),
    ]
