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
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=2)),
        ))
        db.send_create_signal(u'seatmap', ['Seat'])

        # Adding model 'Row'
        db.create_table(u'seatmap_row', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.IntegerField')()),
            ('orientation', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('position_x', self.gf('django.db.models.fields.IntegerField')()),
            ('position_y', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'seatmap', ['Row'])

        # Adding model 'Seatmap'
        db.create_table(u'seatmap_seatmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.LanEvent'])),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'seatmap', ['Seatmap'])

        # Adding M2M table for field rows on 'Seatmap'
        m2m_table_name = db.shorten_name(u'seatmap_seatmap_rows')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('seatmap', models.ForeignKey(orm[u'seatmap.seatmap'], null=False)),
            ('row', models.ForeignKey(orm[u'seatmap.row'], null=False))
        ))
        db.create_unique(m2m_table_name, ['seatmap_id', 'row_id'])

        # Adding model 'RowSeat'
        db.create_table(u'seatmap_rowseat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seatmap.Row'])),
            ('seat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seatmap.Seat'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'seatmap', ['RowSeat'])


    def backwards(self, orm):
        # Deleting model 'Seat'
        db.delete_table(u'seatmap_seat')

        # Deleting model 'Row'
        db.delete_table(u'seatmap_row')

        # Deleting model 'Seatmap'
        db.delete_table(u'seatmap_seatmap')

        # Removing M2M table for field rows on 'Seatmap'
        db.delete_table(db.shorten_name(u'seatmap_seatmap_rows'))

        # Deleting model 'RowSeat'
        db.delete_table(u'seatmap_rowseat')


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
            'Meta': {'object_name': 'Row'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orientation': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'position_x': ('django.db.models.fields.IntegerField', [], {}),
            'position_y': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.IntegerField', [], {})
        },
        u'seatmap.rowseat': {
            'Meta': {'object_name': 'RowSeat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seatmap.Row']"}),
            'seat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['seatmap.Seat']"})
        },
        u'seatmap.seat': {
            'Meta': {'object_name': 'Seat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '2'})
        },
        u'seatmap.seatmap': {
            'Meta': {'object_name': 'Seatmap'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.LanEvent']"}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rows': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['seatmap.Row']", 'symmetrical': 'False'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['seatmap']