# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0017_auto_20150922_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
