# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='content',
        ),
        migrations.AddField(
            model_name='project',
            name='intro',
            field=models.TextField(default=b'', max_length=300, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
    ]
