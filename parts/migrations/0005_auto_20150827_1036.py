# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0004_auto_20150827_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name_fix',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='brandalias',
            name='alias_fix',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
