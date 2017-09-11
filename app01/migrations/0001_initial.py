# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32, unique=True)),
                ('ctime', models.DateTimeField(auto_now_add=True, null=True)),
                ('uptime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('user_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserGroup')),
            ],
        ),
    ]
