# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 05:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20170622_1415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='following',
            new_name='relations',
        ),
    ]
