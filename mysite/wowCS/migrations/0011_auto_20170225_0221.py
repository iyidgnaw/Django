# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 02:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wowCS', '0010_auto_20170225_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='status',
            new_name='ispublic',
        ),
    ]