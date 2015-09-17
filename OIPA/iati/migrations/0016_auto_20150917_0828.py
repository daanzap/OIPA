# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0015_auto_20150914_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitysector',
            name='vocabulary',
            field=models.ForeignKey(default=None, to='iati.SectorVocabulary', null=True),
        ),
        migrations.AlterField(
            model_name='documentlinktitle',
            name='document_link',
            field=models.ForeignKey(related_name='documentlinktitles', to='iati.DocumentLink'),
        ),
    ]
