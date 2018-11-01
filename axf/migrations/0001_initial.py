# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-01 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=60)),
                ('trackid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
    ]