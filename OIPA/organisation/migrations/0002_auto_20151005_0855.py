# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipientorgbudget',
            name='recipient_org',
            field=models.ForeignKey(related_name='recieving_org', to='organisation.Organisation', db_constraint=False),
        ),
    ]
