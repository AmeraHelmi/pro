# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-01 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_shek_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m2awel',
            name='money',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='m2awel',
            name='paid',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='shek',
            name='amount',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='shek',
            name='num',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='shek',
            name='serial',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='action_paid',
            field=models.CharField(max_length=1500),
        ),
    ]
