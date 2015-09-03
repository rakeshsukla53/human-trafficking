# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0003_auto_20150903_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
