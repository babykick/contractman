# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u540d\u79f0')),
                ('province', models.CharField(max_length=30, verbose_name='\u7701\u516c\u53f8')),
                ('branch', models.CharField(max_length=30, verbose_name='\u5206\u516c\u53f8')),
            ],
        ),
    ]
