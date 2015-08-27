# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_auto_20150827_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='descr',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
