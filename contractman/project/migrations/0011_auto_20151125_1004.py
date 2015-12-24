# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20151125_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pm',
            field=models.ForeignKey(default=1, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba', to='company.Member'),
        ),
    ]
