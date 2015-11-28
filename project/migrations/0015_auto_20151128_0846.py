# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_auto_20151127_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_type',
            field=models.CharField(default=b'construction', max_length=30, choices=[('constuction', '\u65bd\u5de5'), ('material', '\u6750\u6599')]),
        ),
        migrations.AlterField(
            model_name='contract',
            name='fund_limit',
            field=models.DecimalField(default=0, verbose_name=b'\xe5\x90\x88\xe5\x90\x8c\xe4\xb8\x8a\xe9\x99\x90\xe9\x87\x91\xe9\xa2\x9d(\xe4\xb8\x87\xe5\x85\x83)', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='contract',
            name='used_fund',
            field=models.DecimalField(default=0, verbose_name=b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90\xe6\x8a\x95\xe8\xb5\x84(\xe4\xb8\x87\xe5\x85\x83)', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.DecimalField(default=0, verbose_name='\u6279\u590d\u5f00\u652f\u8d39\u7528(\u4e07\u5143)', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='construction_cost',
            field=models.DecimalField(default=0, verbose_name='\u65bd\u5de5\u8d39\u7528(\u4e07\u5143)', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='coordination_cost',
            field=models.DecimalField(default=0, verbose_name='\u534f\u8c03\u8d39\u7528(\u4e07\u5143)', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='material_cost',
            field=models.DecimalField(default=0, verbose_name='\u6750\u6599\u8d39\u7528(\u4e07\u5143)', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='other_cost',
            field=models.DecimalField(default=0, verbose_name='\u5176\u4ed6\u8d39\u7528(\u4e07\u5143)', max_digits=8, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='supervision_cost',
            field=models.DecimalField(default=0, verbose_name='\u76d1\u7406\u8d39\u7528(\u4e07\u5143)', max_digits=8, decimal_places=2),
        ),
    ]
