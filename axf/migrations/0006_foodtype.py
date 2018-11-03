# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-02 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0005_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=80)),
                ('typename', models.CharField(max_length=80)),
                ('childtypenames', models.CharField(max_length=80)),
                ('typesort', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]
