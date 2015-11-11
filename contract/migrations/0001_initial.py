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
                ('title', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(max_length=300, verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe5\x86\x85\xe5\xae\xb9')),
            ],
        ),
    ]
