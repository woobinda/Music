# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-23 15:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(
                    blank=True, upload_to='musicians_avatars')),
                ('about', models.TextField(blank=True, max_length=700)),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='MusicianInstrument',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100,
                                          unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='MusicStyle',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100,
                                          unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Video_url',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Video Name')),
                ('url', models.TextField(max_length=100,
                                         verbose_name='URL form YouTube')),
                ('host', models.ForeignKey(blank=True, null=True,
                                           on_delete=django.db.models.deletion.CASCADE, to='musicians.Musician', verbose_name='host')),
            ],
        ),
        migrations.AddField(
            model_name='musician',
            name='instrument',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='musicians.MusicianInstrument', verbose_name='Instrument'),
        ),
        migrations.AddField(
            model_name='musician',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='musicians', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='musician',
            name='playing_style',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='musicians.MusicStyle', verbose_name='Playing style'),
        ),
    ]
