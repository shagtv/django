# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0006_auto_20150827_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cross',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.ForeignKey(related_name='article_cross', to='parts.Article')),
                ('carticle', models.ForeignKey(related_name='carticle_cross', to='parts.Article')),
            ],
            options={
                'db_table': 'crosses',
            },
        ),
    ]
