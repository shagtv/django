# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=50)),
                ('number_fix', models.CharField(max_length=50)),
                ('descr', models.TextField()),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('name_fix', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='brand',
            field=models.ForeignKey(to='parts.Brand'),
        ),
    ]
