# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LanEvent'
        db.create_table(u'event_lanevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('current', self.gf('django.db.models.fields.BooleanField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('numberOfSeats', self.gf('django.db.models.fields.IntegerField')(max_length=200)),
        ))
        db.send_create_signal(u'event', ['LanEvent'])


    def backwards(self, orm):
        # Deleting model 'LanEvent'
        db.delete_table(u'event_lanevent')


    models = {
        u'event.lanevent': {
            'Meta': {'object_name': 'LanEvent'},
            'current': ('django.db.models.fields.BooleanField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'numberOfSeats': ('django.db.models.fields.IntegerField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['event']