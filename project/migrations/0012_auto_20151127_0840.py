# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20151125_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='left_fund',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9c\xaa\xe5\xae\x8c\xe6\x88\x90\xe6\x8a\x95\xe8\xb5\x84(\xe4\xb8\x87\xe5\x85\x83)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='project',
            field=models.ForeignKey(related_name='contracts', to='project.Project'),
        ),
    ]
