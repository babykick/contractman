# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='important',
            field=models.BooleanField(default=False, verbose_name=b'\xe9\x87\x8d\xe8\xa6\x81\xe6\x80\xa7'),
        ),
    ]
