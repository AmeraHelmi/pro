# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20160205_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]
