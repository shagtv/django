# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_cross'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cross',
            unique_together=set([('article', 'carticle')]),
        ),
    ]
