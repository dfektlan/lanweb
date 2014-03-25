# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Seat'
        db.create_table(u'seatmap_seat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seatmap.Row'])),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=2)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'seatmap', ['Seat'])

        # Adding unique constraint on 'Seat', fields ['row', 'number']
        db.create_unique(u'seatmap_seat', ['row_id', 'number'])

        # Adding model 'Row'
        db.create_table(u'seatmap_row', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seatmap', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seatmap.Seatmap'])),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('orientation', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('position_x', self.gf('django.db.models.fields.IntegerField')()),
            ('position_y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'seatmap', ['Row'])

        # Adding unique constraint on 'Row', fields ['seatmap', 'row']
        db.create_unique(u'seatmap_row', ['seatmap_id', 'row'])

        # Adding model 'Seatmap'
        db.create_table(u'seatmap_seatmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.LanEvent'])),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'seatmap', ['Seatmap'])


    def backwards(self, orm):
        # Removing unique constraint on 'Row', fields ['seatmap', 'row']
        db.delete_unique(u'seatmap_row', ['seatmap_id', 'row'])

        # Removing unique constraint on 'Seat', fields ['row', 'number']
        db.delete_unique(u'seatmap_seat', ['row_id', 'number'])

        # Deleting model 'Seat'
        db.delete_table(u'seatmap_seat')

        # Deleting model 'Row'
        db.delete_table(u'seatmap_row')

        # Deleting model 'Seatmap'
        db.delete_table(u'seatmap_seatmap')


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
            'Meta': {'unique_together': "(('seatmap', 'row'),)", 'object_name': 'Row'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientation': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'position_x': ('django.db.models.fields.IntegerField', [], {}),
            'position_y': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.IntegerField', [], {}),
            'seatmap': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seatmap.Seatmap']"})
        },
        u'seatmap.seat': {
            'Meta': {'unique_together': "(('row', 'number'),)", 'object_name': 'Seat'},
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