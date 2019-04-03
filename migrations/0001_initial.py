# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_code', models.CharField(max_length=2, choices=[(b'en', 'English'), (b'de', 'German'), (b'nl', 'Dutch')])),
                ('status', models.CharField(max_length=1, choices=[(b'o', 'open'), (b'a', 'active'), (b'c', 'closed')])),
                ('started_on', models.DateField()),
                ('closed_on', models.DateField()),
            ],
            options={
                'verbose_name': 'Check List',
                'verbose_name_plural': 'Check Lists',
            },
        ),
        migrations.CreateModel(
            name='CheckSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_de', models.TextField(null=True)),
                ('description_nl', models.TextField(null=True)),
                ('info_department', models.BooleanField(default=False)),
                ('info_person', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('done_date', models.DateField()),
                ('checklist', models.ForeignKey(to='chemicals.CheckList')),
            ],
            options={
                'verbose_name': 'Check List Section',
                'verbose_name_plural': 'Check List Sections',
            },
        ),
        migrations.CreateModel(
            name='CheckUsage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100)),
                ('description_en', models.CharField(max_length=100, null=True)),
                ('description_de', models.CharField(max_length=100, null=True)),
                ('description_nl', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Check List Usage',
                'verbose_name_plural': 'Check List Usages',
            },
        ),
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(default=b'', verbose_name='Comment', blank=True)),
                ('comment_en', models.TextField(default=b'', null=True, verbose_name='Comment', blank=True)),
                ('comment_de', models.TextField(default=b'', null=True, verbose_name='Comment', blank=True)),
                ('comment_nl', models.TextField(default=b'', null=True, verbose_name='Comment', blank=True)),
                ('article', models.CharField(max_length=100, null=True, verbose_name='Article Number', blank=True)),
                ('registration_number', models.CharField(max_length=100, null=True, verbose_name='Registration Number', blank=True)),
                ('cas', models.CharField(max_length=100, null=True, verbose_name='CAS', blank=True)),
                ('einecs', models.CharField(max_length=100, null=True, verbose_name='EINECS', blank=True)),
                ('signal', models.CharField(default=b'', max_length=1, verbose_name='Signal', blank=True, choices=[(b'd', 'danger'), (b'w', 'warning'), (b'n', 'no signal')])),
                ('region_de', models.BooleanField(default=True, verbose_name='Region D')),
                ('region_be', models.BooleanField(default=False, verbose_name='Region B')),
                ('archive', models.BooleanField(default=False, verbose_name='Archive')),
                ('needed', models.BooleanField(default=False, verbose_name='Permanently Needed')),
                ('preparation', models.BooleanField(default=False, verbose_name='Preparation')),
                ('components_registered', models.BooleanField(default=False, verbose_name='Components Registered')),
                ('reach_vo', models.BooleanField(default=False, verbose_name='Listed in annex XIV REACH regulation')),
            ],
            options={
                'verbose_name': 'Chemical',
                'verbose_name_plural': 'Chemicals',
            },
        ),
        migrations.CreateModel(
            name='ChemicalName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Chemical', db_index=True)),
                ('name_en', models.CharField(max_length=200, null=True, verbose_name='Chemical', db_index=True)),
                ('name_de', models.CharField(max_length=200, null=True, verbose_name='Chemical', db_index=True)),
                ('name_nl', models.CharField(max_length=200, null=True, verbose_name='Chemical', db_index=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'ChemicalName',
                'verbose_name_plural': 'ChemicalNames',
            },
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(default=b'', verbose_name='Comment', blank=True)),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
            ],
            options={
                'verbose_name': 'Consumer',
                'verbose_name_plural': 'Consumers',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name', db_index=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doctype', models.CharField(max_length=1, verbose_name='Document Type', choices=[(b'f', 'Approval'), (b'i', 'Substance Information')])),
                ('created', models.DateField(verbose_name='Released on', blank=True)),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
                ('file', filer.fields.file.FilerFileField(verbose_name='File', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='ExtendedSafetyDataSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue_date', models.DateField(null=True, verbose_name='Issue Date', blank=True)),
                ('country_code', models.CharField(max_length=2, verbose_name='Country Code', choices=[(b'en', 'English'), (b'de', 'German'), (b'nl', 'Dutch')])),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created on')),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
                ('file', filer.fields.file.FilerFileField(verbose_name='File', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'Extended Safety Data Sheet',
                'verbose_name_plural': 'Extended Safety Data Sheets',
            },
        ),
        migrations.CreateModel(
            name='HPhrase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='H-Phrase')),
                ('description', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_en', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_de', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_nl', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('seveso_relevant', models.BooleanField(default=False, verbose_name='Seveso Relevant')),
                ('cmr', models.IntegerField(default=9, verbose_name='CMR', choices=[(1, 'CMR Category 1A/1B'), (2, 'CMR Category 2'), (9, 'Not CMR relevant')])),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'H-Phrase',
                'verbose_name_plural': 'H-Phrases',
            },
        ),
        migrations.CreateModel(
            name='HPhraseCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_department', models.BooleanField(default=False)),
                ('info_person', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('done_date', models.DateField()),
                ('checklist', models.ForeignKey(to='chemicals.CheckList')),
            ],
            options={
                'verbose_name': 'H-Phrase',
                'verbose_name_plural': 'H-Phrases',
            },
        ),
        migrations.CreateModel(
            name='HPhraseRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.TextField(default=b'', verbose_name='Information', blank=True)),
                ('info_en', models.TextField(default=b'', null=True, verbose_name='Information', blank=True)),
                ('info_de', models.TextField(default=b'', null=True, verbose_name='Information', blank=True)),
                ('info_nl', models.TextField(default=b'', null=True, verbose_name='Information', blank=True)),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
                ('hphrase', models.ForeignKey(verbose_name='H-Phrase', to='chemicals.HPhrase')),
            ],
            options={
                'verbose_name': 'H-Phrase Relation',
                'verbose_name_plural': 'H-Phrase Relations',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('department', models.ForeignKey(verbose_name='Department', to='chemicals.Department')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Title', blank=True)),
                ('academic_title', models.CharField(max_length=100, null=True, verbose_name='Academic Title', blank=True)),
                ('surname', models.CharField(max_length=100, null=True, verbose_name='Surname', blank=True)),
                ('givenname', models.CharField(max_length=200, verbose_name='Given name')),
                ('phone', models.CharField(max_length=100, null=True, verbose_name='Phone', blank=True)),
                ('fax', models.CharField(max_length=100, null=True, verbose_name='Fax', blank=True)),
                ('email', models.CharField(max_length=100, null=True, verbose_name='Email', blank=True)),
            ],
            options={
                'ordering': ('givenname', 'surname'),
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='Pictogram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=100, verbose_name='Code')),
                ('name', models.CharField(max_length=400, verbose_name='Pictogram')),
                ('name_en', models.CharField(max_length=400, null=True, verbose_name='Pictogram')),
                ('name_de', models.CharField(max_length=400, null=True, verbose_name='Pictogram')),
                ('name_nl', models.CharField(max_length=400, null=True, verbose_name='Pictogram')),
                ('image', filer.fields.image.FilerImageField(verbose_name='Image', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'verbose_name': 'Pictogram',
                'verbose_name_plural': 'Pictograms',
            },
        ),
        migrations.CreateModel(
            name='PictogramCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_department', models.BooleanField(default=False)),
                ('info_person', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('done_date', models.DateField()),
                ('checklist', models.ForeignKey(to='chemicals.CheckList')),
                ('done_by', models.ForeignKey(to='chemicals.Person')),
                ('pphrase', models.ForeignKey(to='chemicals.Pictogram')),
            ],
            options={
                'verbose_name': 'Pictogram Check',
                'verbose_name_plural': 'Pictogram Checks',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_de', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_nl', models.CharField(max_length=100, null=True, verbose_name='Name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Plant',
                'verbose_name_plural': 'Plants',
            },
        ),
        migrations.CreateModel(
            name='PPE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_de', models.TextField(null=True)),
                ('description_nl', models.TextField(null=True)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image')),
            ],
            options={
                'verbose_name': 'Personal Protective Equipment (PPE)',
                'verbose_name_plural': 'Personal Protective Equipments (PPE)',
            },
        ),
        migrations.CreateModel(
            name='PPECheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_department', models.BooleanField(default=False)),
                ('info_person', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('done_date', models.DateField()),
                ('checklist', models.ForeignKey(to='chemicals.CheckList')),
                ('done_by', models.ForeignKey(to='chemicals.Person')),
                ('ppe', models.ForeignKey(to='chemicals.PPE')),
            ],
            options={
                'verbose_name': 'PPE Check',
                'verbose_name_plural': 'PPE Checks',
            },
        ),
        migrations.CreateModel(
            name='PPhrase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='P-Phrase')),
                ('description', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_en', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_de', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_nl', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'P-Phrase',
                'verbose_name_plural': 'P-Phrases',
            },
        ),
        migrations.CreateModel(
            name='PPhraseCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_department', models.BooleanField(default=False)),
                ('info_person', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('done_date', models.DateField()),
                ('checklist', models.ForeignKey(to='chemicals.CheckList')),
                ('done_by', models.ForeignKey(to='chemicals.Person')),
                ('pphrase', models.ForeignKey(to='chemicals.PPhrase')),
            ],
            options={
                'verbose_name': 'P-Phrase',
                'verbose_name_plural': 'P-Phrases',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departments', models.ManyToManyField(to='chemicals.Department', verbose_name='Managed Department')),
                ('user', models.OneToOneField(verbose_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'permissions': (('view_she', 'Can see features only visible for SHE members'),),
            },
        ),
        migrations.CreateModel(
            name='ReachDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_code', models.CharField(max_length=2, verbose_name='Country Code', choices=[(b'en', 'English'), (b'de', 'German'), (b'nl', 'Dutch')])),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created on')),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
                ('file', filer.fields.file.FilerFileField(verbose_name='File', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'Reach Document',
                'verbose_name_plural': 'Reach Documents',
            },
        ),
        migrations.CreateModel(
            name='ReachInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', verbose_name='Description', blank=True)),
                ('description_en', models.TextField(default=b'', null=True, verbose_name='Description', blank=True)),
                ('description_de', models.TextField(default=b'', null=True, verbose_name='Description', blank=True)),
                ('description_nl', models.TextField(default=b'', null=True, verbose_name='Description', blank=True)),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
            ],
            options={
                'verbose_name': 'Reach Information',
                'verbose_name_plural': 'Reach Information',
            },
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.TextField(default=b'', blank=True)),
                ('info_en', models.TextField(default=b'', null=True, blank=True)),
                ('info_de', models.TextField(default=b'', null=True, blank=True)),
                ('info_nl', models.TextField(default=b'', null=True, blank=True)),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
            ],
            options={
                'verbose_name': 'Risk',
                'verbose_name_plural': 'Risks',
            },
        ),
        migrations.CreateModel(
            name='RiskIndication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Risk')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Risk')),
                ('name_de', models.CharField(max_length=100, null=True, verbose_name='Risk')),
                ('name_nl', models.CharField(max_length=100, null=True, verbose_name='Risk')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Risk Indication',
                'verbose_name_plural': 'Risk Indications',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=1, verbose_name='Role', choices=[(b'r', b'REACH'), (b'c', 'Chemical')])),
                ('person', models.ForeignKey(verbose_name='Person', to='chemicals.Person')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='RPhrase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='R-Phrase')),
                ('description', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_en', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_de', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_nl', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'R-Phrase',
                'verbose_name_plural': 'R-Phrases',
            },
        ),
        migrations.CreateModel(
            name='SafetyDataSheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue_date', models.DateField(null=True, verbose_name='Issue Date', blank=True)),
                ('country_code', models.CharField(max_length=2, verbose_name='Country Code', choices=[(b'en', 'English'), (b'de', 'German'), (b'nl', 'Dutch')])),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created on')),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
                ('file', filer.fields.file.FilerFileField(verbose_name='File', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'Safety Data Sheet',
                'verbose_name_plural': 'Safety Data Sheets',
            },
        ),
        migrations.CreateModel(
            name='SevesoCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='Seveso Category')),
                ('description', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_en', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_de', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_nl', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Seveso Category',
                'verbose_name_plural': 'Seveso Categories',
            },
        ),
        migrations.CreateModel(
            name='SevesoDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_code', models.CharField(max_length=2, verbose_name='Country Code', choices=[(b'en', 'English'), (b'de', 'German'), (b'nl', 'Dutch')])),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created on')),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
                ('file', filer.fields.file.FilerFileField(verbose_name='File', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'Seveso Document',
                'verbose_name_plural': 'Seveso Documents',
            },
        ),
        migrations.CreateModel(
            name='SevesoInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(default=b'', verbose_name='Description', blank=True)),
                ('description_en', models.TextField(default=b'', null=True, verbose_name='Description', blank=True)),
                ('description_de', models.TextField(default=b'', null=True, verbose_name='Description', blank=True)),
                ('description_nl', models.TextField(default=b'', null=True, verbose_name='Description', blank=True)),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
            ],
            options={
                'verbose_name': 'Seveso Information',
                'verbose_name_plural': 'Seveso Information',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('max_volume', models.CharField(max_length=25, null=True, verbose_name='Volume', blank=True)),
                ('max_unit', models.CharField(max_length=1, verbose_name='Unit', choices=[(b't', 'tons'), (b'k', 'kilogram'), (b'g', 'gram'), (b'c', 'cubic meter'), (b'l', 'liter'), (b'm', 'mililiter'), (b'p', 'pieces')])),
                ('year_volume', models.CharField(max_length=25, null=True, verbose_name='Year Volume', blank=True)),
                ('year_unit', models.CharField(max_length=1, verbose_name='Unit', choices=[(b't', 'tons'), (b'k', 'kilogram'), (b'g', 'gram'), (b'c', 'cubic meter'), (b'l', 'liter'), (b'm', 'mililiter'), (b'p', 'pieces')])),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
                ('location', models.ForeignKey(verbose_name='Location', to='chemicals.Location')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.CreateModel(
            name='StorageClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='Storage Class')),
                ('description', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_en', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_de', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_nl', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Storage Class',
                'verbose_name_plural': 'Storage Classes',
            },
        ),
        migrations.CreateModel(
            name='StorageClassCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_department', models.BooleanField(default=False)),
                ('info_person', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('done_date', models.DateField()),
                ('checklist', models.ForeignKey(to='chemicals.CheckList')),
                ('done_by', models.ForeignKey(to='chemicals.Person')),
                ('pphrase', models.ForeignKey(to='chemicals.PPhrase')),
            ],
            options={
                'verbose_name': 'Storage Class Check',
                'verbose_name_plural': 'Storage Class Checks',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400, verbose_name='Name')),
                ('address', models.TextField(null=True, verbose_name='Address', blank=True)),
                ('country', models.CharField(max_length=100, null=True, verbose_name='Country', blank=True)),
                ('phone', models.CharField(max_length=100, null=True, verbose_name='Phone', blank=True)),
                ('fax', models.CharField(max_length=100, null=True, verbose_name='Fax', blank=True)),
                ('email', models.CharField(max_length=100, null=True, verbose_name='Email', blank=True)),
                ('web', models.CharField(max_length=100, null=True, verbose_name='Web', blank=True)),
                ('info', models.TextField(null=True, verbose_name='Information', blank=True)),
                ('persons', models.ManyToManyField(to='chemicals.Person', verbose_name='Persons', through='chemicals.Role')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='Toxdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tox', models.BooleanField(default=False, verbose_name='Tox')),
                ('oekotox', models.BooleanField(default=False, verbose_name='Oekotox')),
                ('chemical', models.ForeignKey(verbose_name='Chemical', to='chemicals.Chemical')),
                ('supplier', models.ForeignKey(verbose_name='Supplier', to='chemicals.Supplier')),
            ],
            options={
                'verbose_name': 'Tox Oekotox',
                'verbose_name_plural': 'Tox Oekotox',
            },
        ),
        migrations.CreateModel(
            name='WGK',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='WGK')),
                ('description', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_en', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_de', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
                ('description_nl', models.CharField(max_length=400, null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'WGK',
                'verbose_name_plural': 'WGKs',
            },
        ),
        migrations.CreateModel(
            name='WGKCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_department', models.BooleanField(default=False)),
                ('info_person', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('done_date', models.DateField()),
                ('checklist', models.ForeignKey(to='chemicals.CheckList')),
                ('done_by', models.ForeignKey(to='chemicals.Person')),
                ('pphrase', models.ForeignKey(to='chemicals.WGK')),
            ],
            options={
                'verbose_name': 'WGK',
                'verbose_name_plural': 'WGKs',
            },
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('chemicalname_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='chemicals.ChemicalName')),
            ],
            options={
                'verbose_name': 'Name',
                'verbose_name_plural': 'Name',
            },
            bases=('chemicals.chemicalname',),
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('chemicalname_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='chemicals.ChemicalName')),
            ],
            options={
                'verbose_name': 'Synonym',
                'verbose_name_plural': 'Synonyms',
            },
            bases=('chemicals.chemicalname',),
        ),
        migrations.AddField(
            model_name='safetydatasheet',
            name='supplier',
            field=models.ForeignKey(verbose_name='Supplier', to='chemicals.Supplier'),
        ),
        migrations.AddField(
            model_name='role',
            name='supplier',
            field=models.ForeignKey(verbose_name='Supplier', to='chemicals.Supplier'),
        ),
        migrations.AddField(
            model_name='risk',
            name='riskindication',
            field=models.ForeignKey(verbose_name='Risk Indication', to='chemicals.RiskIndication'),
        ),
        migrations.AddField(
            model_name='hphrasecheck',
            name='done_by',
            field=models.ForeignKey(to='chemicals.Person'),
        ),
        migrations.AddField(
            model_name='hphrasecheck',
            name='hphrase',
            field=models.ForeignKey(to='chemicals.HPhrase'),
        ),
        migrations.AddField(
            model_name='extendedsafetydatasheet',
            name='supplier',
            field=models.ForeignKey(verbose_name='Supplier', to='chemicals.Supplier'),
        ),
        migrations.AddField(
            model_name='document',
            name='plant',
            field=models.ForeignKey(to='chemicals.Plant'),
        ),
        migrations.AddField(
            model_name='department',
            name='plant',
            field=models.ForeignKey(verbose_name='Plant', to='chemicals.Plant'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='department',
            field=models.ForeignKey(verbose_name='Department', to='chemicals.Department'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='supplier',
            field=models.ForeignKey(verbose_name='Supplier', to='chemicals.Supplier'),
        ),
        migrations.AddField(
            model_name='chemicalname',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_chemicals.chemicalname_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='departments',
            field=models.ManyToManyField(to='chemicals.Department', verbose_name='Departments', through='chemicals.Consumer', blank=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='hphrases',
            field=models.ManyToManyField(to='chemicals.HPhrase', verbose_name='H-Phrases', through='chemicals.HPhraseRelation', blank=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='locations',
            field=models.ManyToManyField(to='chemicals.Location', verbose_name='Locations', through='chemicals.Stock', blank=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='pictograms',
            field=models.ManyToManyField(to='chemicals.Pictogram', verbose_name='Pictogram', blank=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='pphrases',
            field=models.ManyToManyField(to='chemicals.PPhrase', verbose_name='P-Phrases', blank=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='risks',
            field=models.ManyToManyField(to='chemicals.RiskIndication', verbose_name='Risk Indication', through='chemicals.Risk', blank=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='rphrases',
            field=models.ManyToManyField(to='chemicals.RPhrase', verbose_name='R-Phrases', blank=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='seveso_categories',
            field=models.ManyToManyField(to='chemicals.SevesoCategory', verbose_name='Seveso Categories', blank=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='storage_class',
            field=models.ForeignKey(default=1, verbose_name='Storage Class', to='chemicals.StorageClass'),
        ),
        migrations.AddField(
            model_name='chemical',
            name='suppliers',
            field=models.ManyToManyField(to='chemicals.Supplier', verbose_name='Suppliers', through='chemicals.Consumer', blank=True),
        ),
        migrations.AddField(
            model_name='chemical',
            name='wgk',
            field=models.ForeignKey(default=1, verbose_name='WGK', to='chemicals.WGK'),
        ),
        migrations.AddField(
            model_name='checksection',
            name='done_by',
            field=models.ForeignKey(to='chemicals.Person'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='chemical',
            field=models.ForeignKey(to='chemicals.Chemical'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='closed_by',
            field=models.ForeignKey(related_name='closer', to='chemicals.Person'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='department',
            field=models.ForeignKey(to='chemicals.Department'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='started_by',
            field=models.ForeignKey(related_name='initiator', to='chemicals.Person'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='usage',
            field=models.ForeignKey(to='chemicals.CheckUsage'),
        ),
        migrations.AddField(
            model_name='synonym',
            name='chemical',
            field=models.ForeignKey(related_name='synonyms', default=1, verbose_name='Chemical', to='chemicals.Chemical'),
        ),
        migrations.AddField(
            model_name='identifier',
            name='chemical',
            field=models.OneToOneField(related_name='name', default=1, verbose_name='Chemical', to='chemicals.Chemical'),
        ),
    ]
