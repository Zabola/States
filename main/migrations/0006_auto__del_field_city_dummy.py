# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'City.dummy'
        db.delete_column(u'main_city', 'dummy')


    def backwards(self, orm):
        # Adding field 'City.dummy'
        db.add_column(u'main_city', 'dummy',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True),
                      keep_default=False)


    models = {
        u'main.city': {
            'Meta': {'object_name': 'City'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longtitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.State']", 'null': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'main.statecapital': {
            'Meta': {'object_name': 'StateCapital'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longtitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'population': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['main.State']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['main']