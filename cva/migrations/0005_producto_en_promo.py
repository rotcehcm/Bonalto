# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cva', '0004_auto_20160610_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='en_promo',
            field=models.NullBooleanField(default=False),
        ),
    ]
