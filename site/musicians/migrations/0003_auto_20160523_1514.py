# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-23 15:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0002_auto_20160523_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='musicians', to=settings.AUTH_USER_MODEL),
        ),
    ]
