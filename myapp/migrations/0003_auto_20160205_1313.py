# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160204_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='shek',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='action_date',
            field=models.DateField(),
        ),
    ]
