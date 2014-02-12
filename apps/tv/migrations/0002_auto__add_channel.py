# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Channel'
        db.create_table(u'tv_channel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('channelName', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('displayName', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'tv', ['Channel'])


    def backwards(self, orm):
        # Deleting model 'Channel'
        db.delete_table(u'tv_channel')


    models = {
        u'tv.channel': {
            'Meta': {'object_name': 'Channel'},
            'channelName': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'displayName': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tv']