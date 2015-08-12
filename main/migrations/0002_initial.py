# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StateCapital'
        db.create_table(u'main_statecapital', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('capital', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('longtitude', self.gf('django.db.models.fields.FloatField')()),
            ('capital_population', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'main', ['StateCapital'])

        # Adding model 'State'
        db.create_table(u'main_state', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'main', ['State'])


    def backwards(self, orm):
        # Deleting model 'StateCapital'
        db.delete_table(u'main_statecapital')

        # Deleting model 'State'
        db.delete_table(u'main_state')


    models = {
        u'main.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'main.statecapital': {
            'Meta': {'object_name': 'StateCapital'},
            'capital': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'capital_population': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longtitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['main']