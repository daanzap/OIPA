# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0016_auto_20150917_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='last_updated',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='activity',
            field=models.ForeignKey(related_name='descriptions', to='iati.Activity'),
        ),
        migrations.AlterField(
            model_name='documentlink',
            name='activity',
            field=models.ForeignKey(related_name='documentlinks', to='iati.Activity'),
        ),
        migrations.AlterField(
            model_name='title',
            name='activity',
            field=models.ForeignKey(related_name='titles', to='iati.Activity'),
        ),
    ]
