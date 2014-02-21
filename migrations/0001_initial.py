# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HPhrase'
        db.create_table(u'chemicals_hphrase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('phrase', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('info_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('info_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('info_nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('info_nb', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('seveso_relevant', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('chemicals', ['HPhrase'])

        # Adding model 'PPhrase'
        db.create_table(u'chemicals_pphrase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('phrase', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('chemicals', ['PPhrase'])

        # Adding model 'RPhrase'
        db.create_table(u'chemicals_rphrase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('phrase', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('chemicals', ['RPhrase'])

        # Adding model 'Pictogram'
        db.create_table(u'chemicals_pictogram', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'])),
        ))
        db.send_create_signal('chemicals', ['Pictogram'])

        # Adding model 'SevesoCategory'
        db.create_table(u'chemicals_sevesocategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('chemicals', ['SevesoCategory'])

        # Adding model 'StorageClass'
        db.create_table(u'chemicals_storageclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('classification', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description_de', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description_nl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description_nb', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('chemicals', ['StorageClass'])

        # Adding model 'Synonym'
        db.create_table(u'chemicals_synonym', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('chemicals', ['Synonym'])

        # Adding model 'WGK'
        db.create_table(u'chemicals_wgk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('chemicals', ['WGK'])

        # Adding model 'Risk'
        db.create_table(u'chemicals_risk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('chemicals', ['Risk'])

        # Adding model 'Chemical'
        db.create_table(u'chemicals_chemical', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=800, blank=True)),
            ('comment_en', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('comment_de', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('comment_nl', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('comment_nb', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('article', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('registration_number', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cas', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('einecs', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cmr', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('needed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('preparation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('archive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('instruction', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hazardous', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reach_vo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('components_registered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('replaced', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'], null=True, blank=True)),
        ))
        db.send_create_signal('chemicals', ['Chemical'])

        # Adding M2M table for field risks on 'Chemical'
        m2m_table_name = db.shorten_name(u'chemicals_chemical_risks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chemical', models.ForeignKey(orm['chemicals.chemical'], null=False)),
            ('risk', models.ForeignKey(orm['chemicals.risk'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chemical_id', 'risk_id'])

        # Adding M2M table for field wgks on 'Chemical'
        m2m_table_name = db.shorten_name(u'chemicals_chemical_wgks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chemical', models.ForeignKey(orm['chemicals.chemical'], null=False)),
            ('wgk', models.ForeignKey(orm['chemicals.wgk'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chemical_id', 'wgk_id'])

        # Adding M2M table for field synonyms on 'Chemical'
        m2m_table_name = db.shorten_name(u'chemicals_chemical_synonyms')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chemical', models.ForeignKey(orm['chemicals.chemical'], null=False)),
            ('synonym', models.ForeignKey(orm['chemicals.synonym'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chemical_id', 'synonym_id'])

        # Adding M2M table for field storage_classes on 'Chemical'
        m2m_table_name = db.shorten_name(u'chemicals_chemical_storage_classes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chemical', models.ForeignKey(orm['chemicals.chemical'], null=False)),
            ('storageclass', models.ForeignKey(orm['chemicals.storageclass'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chemical_id', 'storageclass_id'])

        # Adding M2M table for field seveso_categories on 'Chemical'
        m2m_table_name = db.shorten_name(u'chemicals_chemical_seveso_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chemical', models.ForeignKey(orm['chemicals.chemical'], null=False)),
            ('sevesocategory', models.ForeignKey(orm['chemicals.sevesocategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chemical_id', 'sevesocategory_id'])

        # Adding M2M table for field rphrases on 'Chemical'
        m2m_table_name = db.shorten_name(u'chemicals_chemical_rphrases')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chemical', models.ForeignKey(orm['chemicals.chemical'], null=False)),
            ('rphrase', models.ForeignKey(orm['chemicals.rphrase'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chemical_id', 'rphrase_id'])

        # Adding M2M table for field pphrases on 'Chemical'
        m2m_table_name = db.shorten_name(u'chemicals_chemical_pphrases')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chemical', models.ForeignKey(orm['chemicals.chemical'], null=False)),
            ('pphrase', models.ForeignKey(orm['chemicals.pphrase'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chemical_id', 'pphrase_id'])

        # Adding M2M table for field hphrases on 'Chemical'
        m2m_table_name = db.shorten_name(u'chemicals_chemical_hphrases')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chemical', models.ForeignKey(orm['chemicals.chemical'], null=False)),
            ('hphrase', models.ForeignKey(orm['chemicals.hphrase'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chemical_id', 'hphrase_id'])

        # Adding M2M table for field producer on 'Chemical'
        m2m_table_name = db.shorten_name(u'chemicals_chemical_producer')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chemical', models.ForeignKey(orm['chemicals.chemical'], null=False)),
            ('contact', models.ForeignKey(orm['chemicals.contact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['chemical_id', 'contact_id'])

        # Adding model 'Document'
        db.create_table(u'chemicals_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Plant'])),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.File'])),
            ('doctype', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('chemicals', ['Document'])

        # Adding model 'ReachDocument'
        db.create_table(u'chemicals_reachdocument', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.File'])),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('chemicals', ['ReachDocument'])

        # Adding model 'ReachInformation'
        db.create_table(u'chemicals_reachinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_nb', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('chemicals', ['ReachInformation'])

        # Adding model 'SafetyDataSheet'
        db.create_table(u'chemicals_safetydatasheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Contact'])),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.File'])),
            ('instruction', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('issue_date', self.gf('django.db.models.fields.DateField')()),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('chemicals', ['SafetyDataSheet'])

        # Adding model 'ExtendedSafetyDataSheet'
        db.create_table(u'chemicals_extendedsafetydatasheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Contact'])),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.File'])),
            ('instruction', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('issue_date', self.gf('django.db.models.fields.DateField')()),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('chemicals', ['ExtendedSafetyDataSheet'])

        # Adding model 'SevesoDocument'
        db.create_table(u'chemicals_sevesodocument', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.File'])),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('chemicals', ['SevesoDocument'])

        # Adding model 'SevesoInformation'
        db.create_table(u'chemicals_sevesoinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_nb', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('chemicals', ['SevesoInformation'])

        # Adding model 'Signal'
        db.create_table(u'chemicals_signal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('pictogram', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Pictogram'])),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('chemicals', ['Signal'])

        # Adding model 'Person'
        db.create_table(u'chemicals_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('academic_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('givenname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('chemicals', ['Person'])

        # Adding model 'Contact'
        db.create_table(u'chemicals_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('web', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('producer', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('chemicals', ['Contact'])

        # Adding model 'Role'
        db.create_table(u'chemicals_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Person'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Contact'])),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('chemicals', ['Role'])

        # Adding model 'Plant'
        db.create_table(u'chemicals_plant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_nb', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('chemicals', ['Plant'])

        # Adding model 'Department'
        db.create_table(u'chemicals_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Plant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('chemicals', ['Department'])

        # Adding model 'Location'
        db.create_table(u'chemicals_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Department'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('chemicals', ['Location'])

        # Adding model 'Stock'
        db.create_table(u'chemicals_stock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Location'])),
            ('max_volume', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('max_unit', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('year_volume', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('year_unit', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('chemicals', ['Stock'])

        # Adding model 'Supplier'
        db.create_table(u'chemicals_supplier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Contact'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Department'])),
            ('has_instructions', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('chemicals', ['Supplier'])

        # Adding model 'CheckUsage'
        db.create_table(u'chemicals_checkusage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description_de', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description_nl', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description_nb', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('chemicals', ['CheckUsage'])

        # Adding model 'CheckList'
        db.create_table(u'chemicals_checklist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Department'])),
            ('chemical', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Chemical'])),
            ('usage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.CheckUsage'])),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('started_on', self.gf('django.db.models.fields.DateField')()),
            ('started_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='initiator', to=orm['chemicals.Person'])),
            ('closed_on', self.gf('django.db.models.fields.DateField')()),
            ('closed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='closer', to=orm['chemicals.Person'])),
        ))
        db.send_create_signal('chemicals', ['CheckList'])

        # Adding model 'CheckSection'
        db.create_table(u'chemicals_checksection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checklist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.CheckList'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_nb', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('info_department', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done_date', self.gf('django.db.models.fields.DateField')()),
            ('done_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Person'])),
        ))
        db.send_create_signal('chemicals', ['CheckSection'])

        # Adding model 'PPE'
        db.create_table(u'chemicals_ppe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_de', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_nl', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_nb', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Image'])),
        ))
        db.send_create_signal('chemicals', ['PPE'])

        # Adding model 'HPhraseCheck'
        db.create_table(u'chemicals_hphrasecheck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checklist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.CheckList'])),
            ('hphrase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.HPhrase'])),
            ('info_department', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done_date', self.gf('django.db.models.fields.DateField')()),
            ('done_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Person'])),
        ))
        db.send_create_signal('chemicals', ['HPhraseCheck'])

        # Adding model 'PPhraseCheck'
        db.create_table(u'chemicals_pphrasecheck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checklist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.CheckList'])),
            ('pphrase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.PPhrase'])),
            ('info_department', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done_date', self.gf('django.db.models.fields.DateField')()),
            ('done_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Person'])),
        ))
        db.send_create_signal('chemicals', ['PPhraseCheck'])

        # Adding model 'WGKCheck'
        db.create_table(u'chemicals_wgkcheck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checklist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.CheckList'])),
            ('pphrase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.WGK'])),
            ('info_department', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done_date', self.gf('django.db.models.fields.DateField')()),
            ('done_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Person'])),
        ))
        db.send_create_signal('chemicals', ['WGKCheck'])

        # Adding model 'PictogramCheck'
        db.create_table(u'chemicals_pictogramcheck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checklist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.CheckList'])),
            ('pphrase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Pictogram'])),
            ('info_department', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done_date', self.gf('django.db.models.fields.DateField')()),
            ('done_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Person'])),
        ))
        db.send_create_signal('chemicals', ['PictogramCheck'])

        # Adding model 'StorageClassCheck'
        db.create_table(u'chemicals_storageclasscheck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checklist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.CheckList'])),
            ('pphrase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.PPhrase'])),
            ('info_department', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done_date', self.gf('django.db.models.fields.DateField')()),
            ('done_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Person'])),
        ))
        db.send_create_signal('chemicals', ['StorageClassCheck'])

        # Adding model 'PPECheck'
        db.create_table(u'chemicals_ppecheck', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('checklist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.CheckList'])),
            ('ppe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.PPE'])),
            ('info_department', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('done_date', self.gf('django.db.models.fields.DateField')()),
            ('done_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chemicals.Person'])),
        ))
        db.send_create_signal('chemicals', ['PPECheck'])


    def backwards(self, orm):
        # Deleting model 'HPhrase'
        db.delete_table(u'chemicals_hphrase')

        # Deleting model 'PPhrase'
        db.delete_table(u'chemicals_pphrase')

        # Deleting model 'RPhrase'
        db.delete_table(u'chemicals_rphrase')

        # Deleting model 'Pictogram'
        db.delete_table(u'chemicals_pictogram')

        # Deleting model 'SevesoCategory'
        db.delete_table(u'chemicals_sevesocategory')

        # Deleting model 'StorageClass'
        db.delete_table(u'chemicals_storageclass')

        # Deleting model 'Synonym'
        db.delete_table(u'chemicals_synonym')

        # Deleting model 'WGK'
        db.delete_table(u'chemicals_wgk')

        # Deleting model 'Risk'
        db.delete_table(u'chemicals_risk')

        # Deleting model 'Chemical'
        db.delete_table(u'chemicals_chemical')

        # Removing M2M table for field risks on 'Chemical'
        db.delete_table(db.shorten_name(u'chemicals_chemical_risks'))

        # Removing M2M table for field wgks on 'Chemical'
        db.delete_table(db.shorten_name(u'chemicals_chemical_wgks'))

        # Removing M2M table for field synonyms on 'Chemical'
        db.delete_table(db.shorten_name(u'chemicals_chemical_synonyms'))

        # Removing M2M table for field storage_classes on 'Chemical'
        db.delete_table(db.shorten_name(u'chemicals_chemical_storage_classes'))

        # Removing M2M table for field seveso_categories on 'Chemical'
        db.delete_table(db.shorten_name(u'chemicals_chemical_seveso_categories'))

        # Removing M2M table for field rphrases on 'Chemical'
        db.delete_table(db.shorten_name(u'chemicals_chemical_rphrases'))

        # Removing M2M table for field pphrases on 'Chemical'
        db.delete_table(db.shorten_name(u'chemicals_chemical_pphrases'))

        # Removing M2M table for field hphrases on 'Chemical'
        db.delete_table(db.shorten_name(u'chemicals_chemical_hphrases'))

        # Removing M2M table for field producer on 'Chemical'
        db.delete_table(db.shorten_name(u'chemicals_chemical_producer'))

        # Deleting model 'Document'
        db.delete_table(u'chemicals_document')

        # Deleting model 'ReachDocument'
        db.delete_table(u'chemicals_reachdocument')

        # Deleting model 'ReachInformation'
        db.delete_table(u'chemicals_reachinformation')

        # Deleting model 'SafetyDataSheet'
        db.delete_table(u'chemicals_safetydatasheet')

        # Deleting model 'ExtendedSafetyDataSheet'
        db.delete_table(u'chemicals_extendedsafetydatasheet')

        # Deleting model 'SevesoDocument'
        db.delete_table(u'chemicals_sevesodocument')

        # Deleting model 'SevesoInformation'
        db.delete_table(u'chemicals_sevesoinformation')

        # Deleting model 'Signal'
        db.delete_table(u'chemicals_signal')

        # Deleting model 'Person'
        db.delete_table(u'chemicals_person')

        # Deleting model 'Contact'
        db.delete_table(u'chemicals_contact')

        # Deleting model 'Role'
        db.delete_table(u'chemicals_role')

        # Deleting model 'Plant'
        db.delete_table(u'chemicals_plant')

        # Deleting model 'Department'
        db.delete_table(u'chemicals_department')

        # Deleting model 'Location'
        db.delete_table(u'chemicals_location')

        # Deleting model 'Stock'
        db.delete_table(u'chemicals_stock')

        # Deleting model 'Supplier'
        db.delete_table(u'chemicals_supplier')

        # Deleting model 'CheckUsage'
        db.delete_table(u'chemicals_checkusage')

        # Deleting model 'CheckList'
        db.delete_table(u'chemicals_checklist')

        # Deleting model 'CheckSection'
        db.delete_table(u'chemicals_checksection')

        # Deleting model 'PPE'
        db.delete_table(u'chemicals_ppe')

        # Deleting model 'HPhraseCheck'
        db.delete_table(u'chemicals_hphrasecheck')

        # Deleting model 'PPhraseCheck'
        db.delete_table(u'chemicals_pphrasecheck')

        # Deleting model 'WGKCheck'
        db.delete_table(u'chemicals_wgkcheck')

        # Deleting model 'PictogramCheck'
        db.delete_table(u'chemicals_pictogramcheck')

        # Deleting model 'StorageClassCheck'
        db.delete_table(u'chemicals_storageclasscheck')

        # Deleting model 'PPECheck'
        db.delete_table(u'chemicals_ppecheck')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'chemicals.checklist': {
            'Meta': {'object_name': 'CheckList'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'closed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'closer'", 'to': "orm['chemicals.Person']"}),
            'closed_on': ('django.db.models.fields.DateField', [], {}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'started_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'initiator'", 'to': "orm['chemicals.Person']"}),
            'started_on': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'usage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.CheckUsage']"})
        },
        'chemicals.checksection': {
            'Meta': {'object_name': 'CheckSection'},
            'checklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.CheckList']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'done_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Person']"}),
            'done_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_department': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'info_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'chemicals.checkusage': {
            'Meta': {'object_name': 'CheckUsage'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description_nb': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'chemicals.chemical': {
            'Meta': {'object_name': 'Chemical'},
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'article': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cmr': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '800', 'blank': 'True'}),
            'comment_de': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'comment_en': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'comment_nb': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'comment_nl': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'components_registered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'departments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.Department']", 'symmetrical': 'False', 'through': "orm['chemicals.Supplier']", 'blank': 'True'}),
            'einecs': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'hazardous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hphrases': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.HPhrase']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.Location']", 'symmetrical': 'False', 'through': "orm['chemicals.Stock']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'needed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pictograms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.Pictogram']", 'symmetrical': 'False', 'through': "orm['chemicals.Signal']", 'blank': 'True'}),
            'pphrases': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.PPhrase']", 'symmetrical': 'False', 'blank': 'True'}),
            'preparation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'producer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.Contact']", 'symmetrical': 'False', 'blank': 'True'}),
            'reach_vo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registration_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'replaced': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']", 'null': 'True', 'blank': 'True'}),
            'risks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.Risk']", 'symmetrical': 'False', 'blank': 'True'}),
            'rphrases': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.RPhrase']", 'symmetrical': 'False', 'blank': 'True'}),
            'seveso_categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.SevesoCategory']", 'symmetrical': 'False', 'blank': 'True'}),
            'storage_classes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.StorageClass']", 'symmetrical': 'False', 'blank': 'True'}),
            'synonyms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.Synonym']", 'symmetrical': 'False', 'blank': 'True'}),
            'wgks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.WGK']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'chemicals.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'persons': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.Person']", 'through': "orm['chemicals.Role']", 'symmetrical': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'producer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'chemicals.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'plant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Plant']"})
        },
        'chemicals.document': {
            'Meta': {'object_name': 'Document'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'doctype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Plant']"})
        },
        'chemicals.extendedsafetydatasheet': {
            'Meta': {'object_name': 'ExtendedSafetyDataSheet'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'issue_date': ('django.db.models.fields.DateField', [], {}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Contact']"})
        },
        'chemicals.hphrase': {
            'Meta': {'object_name': 'HPhrase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'info_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_nb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'phrase': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'seveso_relevant': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'chemicals.hphrasecheck': {
            'Meta': {'object_name': 'HPhraseCheck'},
            'checklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.CheckList']"}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'done_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Person']"}),
            'done_date': ('django.db.models.fields.DateField', [], {}),
            'hphrase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.HPhrase']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_department': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'info_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'chemicals.location': {
            'Meta': {'object_name': 'Location'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'chemicals.person': {
            'Meta': {'object_name': 'Person'},
            'academic_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'givenname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'chemicals.pictogram': {
            'Meta': {'object_name': 'Pictogram'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        },
        'chemicals.pictogramcheck': {
            'Meta': {'object_name': 'PictogramCheck'},
            'checklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.CheckList']"}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'done_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Person']"}),
            'done_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_department': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'info_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pphrase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Pictogram']"})
        },
        'chemicals.plant': {
            'Meta': {'object_name': 'Plant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'chemicals.ppe': {
            'Meta': {'object_name': 'PPE'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']"})
        },
        'chemicals.ppecheck': {
            'Meta': {'object_name': 'PPECheck'},
            'checklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.CheckList']"}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'done_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Person']"}),
            'done_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_department': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'info_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ppe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.PPE']"})
        },
        'chemicals.pphrase': {
            'Meta': {'object_name': 'PPhrase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'phrase': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'chemicals.pphrasecheck': {
            'Meta': {'object_name': 'PPhraseCheck'},
            'checklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.CheckList']"}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'done_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Person']"}),
            'done_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_department': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'info_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pphrase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.PPhrase']"})
        },
        'chemicals.reachdocument': {
            'Meta': {'object_name': 'ReachDocument'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'chemicals.reachinformation': {
            'Meta': {'object_name': 'ReachInformation'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'chemicals.risk': {
            'Meta': {'object_name': 'Risk'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'chemicals.role': {
            'Meta': {'object_name': 'Role'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Person']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'chemicals.rphrase': {
            'Meta': {'object_name': 'RPhrase'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'phrase': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'chemicals.safetydatasheet': {
            'Meta': {'object_name': 'SafetyDataSheet'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'issue_date': ('django.db.models.fields.DateField', [], {}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Contact']"})
        },
        'chemicals.sevesocategory': {
            'Meta': {'object_name': 'SevesoCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'chemicals.sevesodocument': {
            'Meta': {'object_name': 'SevesoDocument'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'chemicals.sevesoinformation': {
            'Meta': {'object_name': 'SevesoInformation'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'chemicals.signal': {
            'Meta': {'object_name': 'Signal'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pictogram': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Pictogram']"}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'chemicals.stock': {
            'Meta': {'object_name': 'Stock'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Location']"}),
            'max_unit': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'max_volume': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'year_unit': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'year_volume': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'chemicals.storageclass': {
            'Meta': {'object_name': 'StorageClass'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description_de': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description_nb': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'chemicals.storageclasscheck': {
            'Meta': {'object_name': 'StorageClassCheck'},
            'checklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.CheckList']"}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'done_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Person']"}),
            'done_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_department': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'info_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pphrase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.PPhrase']"})
        },
        'chemicals.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Contact']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Department']"}),
            'has_instructions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'chemicals.synonym': {
            'Meta': {'object_name': 'Synonym'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'chemicals.wgk': {
            'Meta': {'object_name': 'WGK'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nb': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'chemicals.wgkcheck': {
            'Meta': {'object_name': 'WGKCheck'},
            'checklist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.CheckList']"}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'done_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Person']"}),
            'done_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_department': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'info_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pphrase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.WGK']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['chemicals']