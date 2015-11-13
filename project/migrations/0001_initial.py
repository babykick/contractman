# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial_number', models.CharField(unique=True, max_length=50, verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe7\xbc\x96\xe5\x8f\xb7')),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe5\x90\x8d\xe7\xa7\xb0')),
                ('content', models.TextField(max_length=300, verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe5\x86\x85\xe5\xae\xb9')),
                ('fund', models.IntegerField(verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe4\xb8\x8a\xe9\x99\x90\xe9\x87\x91\xe9\xa2\x9d(\xe4\xb8\x87\xe5\x85\x83)')),
                ('important', models.BooleanField(default=False, verbose_name=b'\xe9\x87\x8d\xe8\xa6\x81\xe6\x80\xa7')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial_number', models.CharField(unique=True, max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xbc\x96\xe5\x8f\xb7')),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('content', models.TextField(max_length=300, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x86\x85\xe5\xae\xb9')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial_number', models.CharField(unique=True, max_length=50, verbose_name=b'\xe5\xb7\xa5\xe5\x8d\x95\xe7\xbc\x96\xe5\x8f\xb7')),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\xb7\xa5\xe5\x8d\x95\xe5\x90\x8d')),
                ('content', models.CharField(max_length=1000, verbose_name=b'\xe5\xb7\xa5\xe5\x8d\x95\xe5\x86\x85\xe5\xae\xb9')),
                ('budget', models.PositiveIntegerField(verbose_name=b'\xe5\xb7\xa5\xe5\x8d\x95\xe9\xa2\x84\xe7\xae\x97')),
                ('contract', models.ForeignKey(to='project.Contract')),
            ],
        ),
    ]
