# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-02 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0006_foodtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20)),
                ('productimg', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=50)),
                ('productlongname', models.CharField(max_length=100)),
                ('isxf', models.BooleanField(default=0)),
                ('pmdesc', models.BooleanField(default=0)),
                ('specifics', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('marketprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=100)),
                ('dealerid', models.CharField(max_length=20)),
                ('storenums', models.CharField(max_length=20)),
                ('productnum', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]