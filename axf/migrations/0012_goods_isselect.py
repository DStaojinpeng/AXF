# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-08 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0011_cart_isselect'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='isselect',
            field=models.BooleanField(default=False),
        ),
    ]
