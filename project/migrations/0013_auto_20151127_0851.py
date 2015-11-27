# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20151127_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='left_fund',
        ),
        migrations.AddField(
            model_name='contract',
            name='used_fund',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90\xe6\x8a\x95\xe8\xb5\x84(\xe4\xb8\x87\xe5\x85\x83)'),
            preserve_default=False,
        ),
    ]
