# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowCS', '0002_auto_20170222_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_content',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
