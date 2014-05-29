# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'page_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'page', ['Page'])

        # Adding M2M table for field events on 'Page'
        m2m_table_name = db.shorten_name(u'page_page_events')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'page.page'], null=False)),
            ('lanevent', models.ForeignKey(orm[u'event.lanevent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['page_id', 'lanevent_id'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'page_page')

        # Removing M2M table for field events on 'Page'
        db.delete_table(db.shorten_name(u'page_page_events'))


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
            'shortname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'page.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['event.LanEvent']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['page']