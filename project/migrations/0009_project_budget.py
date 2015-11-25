# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20151119_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
