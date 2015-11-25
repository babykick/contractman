# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_member_department'),
        ('project', '0009_project_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='construction_cost',
            field=models.PositiveIntegerField(default=0, verbose_name='\u65bd\u5de5\u8d39\u7528(\u4e07\u5143)'),
        ),
        migrations.AddField(
            model_name='project',
            name='coordination_cost',
            field=models.PositiveIntegerField(default=0, verbose_name='\u534f\u8c03\u8d39\u7528(\u4e07\u5143)'),
        ),
        migrations.AddField(
            model_name='project',
            name='material_cost',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6750\u6599\u8d39\u7528(\u4e07\u5143)'),
        ),
        migrations.AddField(
            model_name='project',
            name='other_cost',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5176\u4ed6\u8d39\u7528(\u4e07\u5143)'),
        ),
        migrations.AddField(
            model_name='project',
            name='pm',
            field=models.ForeignKey(default=1, to='company.Member'),
        ),
        migrations.AddField(
            model_name='project',
            name='supervision_cost',
            field=models.PositiveIntegerField(default=0, verbose_name='\u76d1\u7406\u8d39\u7528(\u4e07\u5143)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6279\u590d\u5f00\u652f\u8d39\u7528(\u4e07\u5143)'),
        ),
    ]
