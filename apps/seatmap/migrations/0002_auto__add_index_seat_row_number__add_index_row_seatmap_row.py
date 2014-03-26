# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Seat', fields ['row', 'number']
        db.create_index(u'seatmap_seat', ['row_id', 'number'])

        # Adding index on 'Row', fields ['seatmap', 'row']
        db.create_index(u'seatmap_row', ['seatmap_id', 'row'])


    def backwards(self, orm):
        # Removing index on 'Row', fields ['seatmap', 'row']
        db.delete_index(u'seatmap_row', ['seatmap_id', 'row'])

        # Removing index on 'Seat', fields ['row', 'number']
        db.delete_index(u'seatmap_seat', ['row_id', 'number'])


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
        },
        u'seatmap.row': {
            'Meta': {'unique_together': "(('seatmap', 'row'),)", 'object_name': 'Row', 'index_together': "[['seatmap', 'row']]"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientation': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'position_x': ('django.db.models.fields.IntegerField', [], {}),
            'position_y': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.IntegerField', [], {}),
            'seatmap': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seatmap.Seatmap']"})
        },
        u'seatmap.seat': {
            'Meta': {'unique_together': "(('row', 'number'),)", 'object_name': 'Seat', 'index_together': "[['row', 'number']]"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seatmap.Row']"}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'})
        },
        u'seatmap.seatmap': {
            'Meta': {'object_name': 'Seatmap'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.LanEvent']"}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['seatmap']