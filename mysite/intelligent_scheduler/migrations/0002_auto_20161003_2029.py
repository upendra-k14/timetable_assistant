# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intelligent_scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rollnumber',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]