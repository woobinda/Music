# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-19 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_auto_20160519_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(
                blank=True, null=True, upload_to=b'users_avatars'),
        ),
    ]
