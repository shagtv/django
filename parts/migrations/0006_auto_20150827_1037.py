# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_auto_20150827_1036'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('brand', 'number_fix')]),
        ),
    ]
