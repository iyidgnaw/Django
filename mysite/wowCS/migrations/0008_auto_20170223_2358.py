# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 23:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wowCS', '0007_auto_20170223_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='notebook_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterUniqueTogether(
            name='notebook',
            unique_together=set([('user', 'notebook_title')]),
        ),
    ]