# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0002_region_region_vocabulary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
    ]
