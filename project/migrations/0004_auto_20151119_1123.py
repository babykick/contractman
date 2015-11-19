# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_contract_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='timeline',
            field=models.DateTimeField(verbose_name=b'\xe6\x97\xb6\xe9\x99\x90(\xe5\xb9\xb4-\xe6\x9c\x88-\xe6\x97\xa5)'),
        ),
    ]
