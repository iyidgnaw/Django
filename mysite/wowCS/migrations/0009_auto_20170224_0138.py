# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowCS', '0008_auto_20170223_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='genre',
            field=models.CharField(default='Not Classified', max_length=100),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='notebook_description',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
