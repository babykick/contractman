# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='fund',
            new_name='fundlimit',
        ),
        migrations.AddField(
            model_name='contract',
            name='partA',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='partB',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='timeline',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
