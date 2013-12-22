# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LanEvent.location'
        db.add_column(u'event_lanevent', 'location',
                      self.gf('django.db.models.fields.CharField')(default='derp', max_length=200),
                      keep_default=False)

        # Adding field 'LanEvent.price'
        db.add_column(u'event_lanevent', 'price',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'LanEvent.numberOfSeats'
        db.add_column(u'event_lanevent', 'numberOfSeats',
                      self.gf('django.db.models.fields.IntegerField')(default=1, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LanEvent.location'
        db.delete_column(u'event_lanevent', 'location')

        # Deleting field 'LanEvent.price'
        db.delete_column(u'event_lanevent', 'price')

        # Deleting field 'LanEvent.numberOfSeats'
        db.delete_column(u'event_lanevent', 'numberOfSeats')


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