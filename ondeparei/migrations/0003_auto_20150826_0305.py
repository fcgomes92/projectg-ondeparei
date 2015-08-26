# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ondeparei', '0002_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 3, 5, 23, 584580, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mark',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 3, 5, 35, 484541, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 3, 5, 37, 831842, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 26, 3, 5, 39, 507322, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
