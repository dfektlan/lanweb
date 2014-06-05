# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Sponsor.event'
        db.delete_column(u'sponsor_sponsor', 'event_id')

        # Adding M2M table for field event on 'Sponsor'
        m2m_table_name = db.shorten_name(u'sponsor_sponsor_event')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sponsor', models.ForeignKey(orm[u'sponsor.sponsor'], null=False)),
            ('lanevent', models.ForeignKey(orm[u'event.lanevent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sponsor_id', 'lanevent_id'])


    def backwards(self, orm):
        # Adding field 'Sponsor.event'
        db.add_column(u'sponsor_sponsor', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2014, 6, 4, 0, 0), related_name='Event', to=orm['event.LanEvent']),
                      keep_default=False)

        # Removing M2M table for field event on 'Sponsor'
        db.delete_table(db.shorten_name(u'sponsor_sponsor_event'))


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
        u'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['event.LanEvent']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'logo_svg': ('django.db.models.fields.files.FileField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['sponsor']