# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regform', '0002_member_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='full_name',
            field=models.CharField(max_length=60, verbose_name='Full name:'),
        ),
    ]