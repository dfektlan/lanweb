# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemGroup'
        db.create_table(u'pos_itemgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'pos', ['ItemGroup'])

        # Adding model 'Item'
        db.create_table(u'pos_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pos.ItemGroup'])),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pos', ['Item'])

        # Adding model 'Order'
        db.create_table(u'pos_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.LanEvent'])),
            ('paymentMethod', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'pos', ['Order'])

        # Adding model 'ItemPack'
        db.create_table(u'pos_itempack', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pos.ItemGroup'])),
        ))
        db.send_create_signal(u'pos', ['ItemPack'])

        # Adding M2M table for field items on 'ItemPack'
        m2m_table_name = db.shorten_name(u'pos_itempack_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('itempack', models.ForeignKey(orm[u'pos.itempack'], null=False)),
            ('item', models.ForeignKey(orm[u'pos.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['itempack_id', 'item_id'])

        # Adding model 'ItemQuantity'
        db.create_table(u'pos_itemquantity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pos.Order'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pos.Item'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pos', ['ItemQuantity'])


    def backwards(self, orm):
        # Deleting model 'ItemGroup'
        db.delete_table(u'pos_itemgroup')

        # Deleting model 'Item'
        db.delete_table(u'pos_item')

        # Deleting model 'Order'
        db.delete_table(u'pos_order')

        # Deleting model 'ItemPack'
        db.delete_table(u'pos_itempack')

        # Removing M2M table for field items on 'ItemPack'
        db.delete_table(db.shorten_name(u'pos_itempack_items'))

        # Deleting model 'ItemQuantity'
        db.delete_table(u'pos_itemquantity')


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
        u'pos.item': {
            'Meta': {'object_name': 'Item'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pos.ItemGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pos.itemgroup': {
            'Meta': {'object_name': 'ItemGroup'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'pos.itempack': {
            'Meta': {'object_name': 'ItemPack'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pos.ItemGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pos.Item']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'pos.itemquantity': {
            'Meta': {'object_name': 'ItemQuantity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pos.Item']"}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pos.Order']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'pos.order': {
            'Meta': {'object_name': 'Order'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.LanEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pos.Item']", 'null': 'True', 'through': u"orm['pos.ItemQuantity']", 'symmetrical': 'False'}),
            'paymentMethod': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['pos']