# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20151119_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='project',
            field=models.ForeignKey(default=None, to='project.Project'),
            preserve_default=False,
        ),
    ]
