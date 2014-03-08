# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Sponsor.logo'
        db.delete_column(u'sponsor_sponsor', 'logo')

        # Adding field 'Sponsor.logo_img'
        db.add_column(u'sponsor_sponsor', 'logo_img',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Sponsor.logo_svg'
        db.add_column(u'sponsor_sponsor', 'logo_svg',
                      self.gf('django.db.models.fields.files.FileField')(max_length=150, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Sponsor.logo'
        db.add_column(u'sponsor_sponsor', 'logo',
                      self.gf('django.db.models.fields.files.ImageField')(default='deprecated', max_length=150),
                      keep_default=False)

        # Deleting field 'Sponsor.logo_img'
        db.delete_column(u'sponsor_sponsor', 'logo_img')

        # Deleting field 'Sponsor.logo_svg'
        db.delete_column(u'sponsor_sponsor', 'logo_svg')


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
        u'sponsor.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Event'", 'to': u"orm['event.LanEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'logo_svg': ('django.db.models.fields.files.FileField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['sponsor']