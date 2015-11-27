# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_auto_20151127_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='fundlimit',
            new_name='fund_limit',
        ),
    ]
