# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 11:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('walletapp', '0004_auto_20171123_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalance',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
