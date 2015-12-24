# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20151119_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='department',
            field=models.ForeignKey(related_name='projects', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe9\x83\xa8\xe9\x97\xa8', to='company.Department', null=True),
        ),
    ]
