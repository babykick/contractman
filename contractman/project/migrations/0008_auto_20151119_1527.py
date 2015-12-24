# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_contract_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='partA',
            field=models.CharField(max_length=50, verbose_name=b'\xe7\x94\xb2\xe6\x96\xb9'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='partB',
            field=models.CharField(max_length=50, verbose_name=b'\xe4\xb9\x99\xe6\x96\xb9'),
        ),
    ]
