# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geodata', '0002_region_region_vocabulary'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('iati', '0019_auto_20150929_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetLine',
            fields=[
                ('object_id', models.CharField(max_length=250, null=True, verbose_name=b'related object')),
                ('ref', models.CharField(max_length=150, serialize=False, primary_key=True)),
                ('value', models.DecimalField(default=None, null=True, max_digits=12, decimal_places=2)),
                ('content_type', models.ForeignKey(verbose_name=b'xml Parent', blank=True, to='contenttypes.ContentType', null=True)),
                ('currency', models.ForeignKey(to='iati.Currency')),
                ('language', models.ForeignKey(default=None, to='iati.Language', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.TextField(max_length=500)),
                ('categories', models.ManyToManyField(related_name='doc_categories', to='iati.DocumentCategory')),
                ('file_format', models.ForeignKey(related_name='file_formats', default=None, to='iati.FileFormat', null=True)),
                ('language', models.ForeignKey(related_name='languages', default=None, to='iati.Language', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentLinkTitle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document_link', models.ForeignKey(related_name='documentlinktitles', to='organisation.DocumentLink')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Narrative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.CharField(max_length=250, null=True, verbose_name=b'related object')),
                ('organisation_identifier', models.CharField(max_length=150, null=True, verbose_name=b'iati_identifier')),
                ('content', models.TextField(null=True, blank=True)),
                ('content_type', models.ForeignKey(related_name='narratives', verbose_name=b'xml Parent', blank=True, to='contenttypes.ContentType', null=True)),
                ('language', models.ForeignKey(related_name='narratives_for_lang', default=None, to='iati.Language', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('code', models.CharField(max_length=250, serialize=False, primary_key=True)),
                ('abbreviation', models.CharField(default=b'', max_length=120)),
                ('organisation_identifier', models.CharField(max_length=150, null=True, verbose_name=b'organisation_identifier')),
                ('original_ref', models.CharField(default=b'', max_length=120)),
                ('last_updated_datetime', models.DateTimeField(null=True)),
                ('iati_version', models.ForeignKey(to='iati.Version')),
                ('type', models.ForeignKey(related_name='organisations', default=None, to='iati.OrganisationType', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipientCountryBudget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period_start', models.DateField(null=True)),
                ('period_end', models.DateField(null=True)),
                ('value', models.DecimalField(default=None, null=True, max_digits=12, decimal_places=2)),
                ('country', models.ForeignKey(to='geodata.Country')),
                ('currency', models.ForeignKey(to='iati.Currency')),
                ('organisation', models.ForeignKey(to='organisation.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='RecipientOrgBudget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period_start', models.DateField(null=True)),
                ('period_end', models.DateField(null=True)),
                ('value', models.DecimalField(default=None, null=True, max_digits=12, decimal_places=2)),
                ('currency', models.ForeignKey(to='iati.Currency')),
                ('organisation', models.ForeignKey(related_name='donor_org', to='organisation.Organisation')),
                ('recipient_org', models.ForeignKey(related_name='recieving_org', to='organisation.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='ReportingOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('secondary_reporter', models.BooleanField(default=False)),
                ('org_type', models.ForeignKey(default=None, to='iati.OrganisationType', null=True)),
                ('organisation', models.ForeignKey(related_name='reporting_orgs', to='organisation.Organisation')),
                ('reporting_org', models.ForeignKey(related_name='reported_by_orgs', to='organisation.Organisation', db_constraint=False)),
            ],
        ),
        migrations.CreateModel(
            name='TotalBudget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period_start', models.DateField(null=True)),
                ('period_end', models.DateField(null=True)),
                ('value', models.DecimalField(default=None, null=True, max_digits=12, decimal_places=2)),
                ('currency', models.ForeignKey(to='iati.Currency')),
                ('organisation', models.ForeignKey(to='organisation.Organisation')),
            ],
        ),
        migrations.AddField(
            model_name='name',
            name='organisation',
            field=models.ForeignKey(to='organisation.Organisation'),
        ),
        migrations.AddField(
            model_name='documentlink',
            name='organisation',
            field=models.ForeignKey(related_name='documentlinks', to='organisation.Organisation'),
        ),
        migrations.AddField(
            model_name='documentlink',
            name='recipient_countries',
            field=models.ManyToManyField(related_name='recipient_countries', to='geodata.Country', blank=True),
        ),
    ]
