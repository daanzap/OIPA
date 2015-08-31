# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0004_auto_20150817_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityscope',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='activitystatus',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='aidtypeflag',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='budgetidentifiersectorcategory',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='budgetidentifiervocabulary',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='budgettype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='collaborationtype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='conditiontype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='contacttype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='descriptiontype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='disbursementchannel',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='geographicalprecision',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='geographicexactness',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='geographiclocationclass',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='geographiclocationreach',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='loanrepaymentperiod',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='loanrepaymenttype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='organisationtype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='policymarker',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='policysignificance',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='publishertype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='regionvocabulary',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='relatedactivity',
            name='related_activity',
            field=models.ForeignKey(related_name='related_activity', on_delete=django.db.models.deletion.SET_NULL, default=None, to='iati.Activity', null=True),
        ),
        migrations.AlterField(
            model_name='relatedactivitytype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='resultindicatormeasure',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='resulttype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='tiedstatus',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='verificationstatus',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
    ]
