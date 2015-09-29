# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0018_auto_20150922_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='is_searchable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='provider_organisation',
            field=models.ForeignKey(related_name='transaction_provider_org', to='iati.TransactionProvider', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='receiver_organisation',
            field=models.ForeignKey(related_name='transaction_receiver_org', to='iati.TransactionReceiver', null=True),
        ),
    ]
