# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iati', '0005_auto_20150831_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financetype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='financetypecategory',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='flowtype',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='sector',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='sectorcategory',
            name='code',
            field=models.CharField(max_length=100, serialize=False, primary_key=True),
        ),
    ]
