# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-26 00:13
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
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_str', models.CharField(max_length=200)),
                ('screen_name', models.CharField(max_length=200)),
                ('url', models.URLField(null=True)),
                ('location', models.CharField(null=True, max_length=200)),
                ('description', models.CharField(null=True, max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
