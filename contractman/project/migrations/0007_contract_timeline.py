# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_remove_contract_timeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='timeline',
            field=models.CharField(default='', max_length=30, verbose_name=b'\xe6\x97\xb6\xe9\x99\x90(\xe5\xb9\xb4-\xe6\x9c\x88-\xe6\x97\xa5)'),
            preserve_default=False,
        ),
    ]
