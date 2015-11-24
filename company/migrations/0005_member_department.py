# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='department',
            field=models.ForeignKey(to='company.Department', null=True),
        ),
    ]
