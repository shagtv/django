# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0002_brandalias'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandalias',
            name='alias_fix',
            field=models.CharField(default=datetime.datetime(2015, 8, 27, 9, 53, 24, 700370, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='descr',
            field=models.TextField(default=b''),
        ),
    ]
