# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SevesoCategory.name_nb'
        db.delete_column(u'chemicals_sevesocategory', 'name_nb')

        # Deleting field 'SevesoCategory.name_de'
        db.delete_column(u'chemicals_sevesocategory', 'name_de')

        # Deleting field 'SevesoCategory.name_en'
        db.delete_column(u'chemicals_sevesocategory', 'name_en')

        # Deleting field 'SevesoCategory.name_nl'
        db.delete_column(u'chemicals_sevesocategory', 'name_nl')

        # Adding field 'SevesoCategory.description'
        db.add_column(u'chemicals_sevesocategory', 'description',
                      self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SevesoCategory.description_en'
        db.add_column(u'chemicals_sevesocategory', 'description_en',
                      self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SevesoCategory.description_de'
        db.add_column(u'chemicals_sevesocategory', 'description_de',
                      self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SevesoCategory.description_nl'
        db.add_column(u'chemicals_sevesocategory', 'description_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SevesoCategory.description_nb'
        db.add_column(u'chemicals_sevesocategory', 'description_nb',
                      self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True),
                      keep_default=False)


        # Changing field 'SevesoCategory.name'
        db.alter_column(u'chemicals_sevesocategory', 'name', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):
        # Adding field 'SevesoCategory.name_nb'
        db.add_column(u'chemicals_sevesocategory', 'name_nb',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SevesoCategory.name_de'
        db.add_column(u'chemicals_sevesocategory', 'name_de',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SevesoCategory.name_en'
        db.add_column(u'chemicals_sevesocategory', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SevesoCategory.name_nl'
        db.add_column(u'chemicals_sevesocategory', 'name_nl',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SevesoCategory.description'
        db.delete_column(u'chemicals_sevesocategory', 'description')

        # Deleting field 'SevesoCategory.description_en'
        db.delete_column(u'chemicals_sevesocategory', 'description_en')

        # Deleting field 'SevesoCategory.description_de'
        db.delete_column(u'chemicals_sevesocategory', 'description_de')

        # Deleting field 'SevesoCategory.description_nl'
        db.delete_column(u'chemicals_sevesocategory', 'description_nl')

        # Deleting field 'SevesoCategory.description_nb'
        db.delete_column(u'chemicals_sevesocategory', 'description_nb')


        # Changing field 'SevesoCategory.name'
        db.alter_column(u'chemicals_sevesocategory', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'article': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cmr': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'comment_de': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'comment_en': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'comment_nb': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'comment_nl': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'components_registered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'departments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.Department']", 'symmetrical': 'False', 'through': "orm['chemicals.Supplier']", 'blank': 'True'}),
            'einecs': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hazardous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hphrases': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.HPhrase']", 'symmetrical': 'False', 'through': "orm['chemicals.HPhraseRelation']", 'blank': 'True'}),
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
            'registration_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'replaced': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']", 'null': 'True', 'blank': 'True'}),
            'risks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['chemicals.RiskIndication']", 'symmetrical': 'False', 'through': "orm['chemicals.Risk']", 'blank': 'True'}),
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
        'chemicals.hphraserelation': {
            'Meta': {'object_name': 'HPhraseRelation'},
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            'hphrase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.HPhrase']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'info_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_nb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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
            'chemical': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.Chemical']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'info_de': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_nb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_nl': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'riskindication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chemicals.RiskIndication']"})
        },
        'chemicals.riskindication': {
            'Meta': {'object_name': 'RiskIndication'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'description_de': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'description_nb': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'description_de': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'description_nb': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
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
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description_de': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description_nb': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description_nl': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
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