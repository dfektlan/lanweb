# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemQuantity'
        db.create_table(u'pos_itemquantity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pos.Order'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pos.Item'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'pos', ['ItemQuantity'])

        # Removing M2M table for field item on 'Order'
        db.delete_table(db.shorten_name(u'pos_order_item'))


    def backwards(self, orm):
        # Deleting model 'ItemQuantity'
        db.delete_table(u'pos_itemquantity')

        # Adding M2M table for field item on 'Order'
        m2m_table_name = db.shorten_name(u'pos_order_item')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm[u'pos.order'], null=False)),
            ('item', models.ForeignKey(orm[u'pos.item'], null=False))
        ))
        db.create_unique(m2m_table_name, ['order_id', 'item_id'])


    models = {
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pos.Item']", 'null': 'True', 'through': u"orm['pos.ItemQuantity']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['pos']