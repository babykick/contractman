# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20151128_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='important',
        ),
    ]
