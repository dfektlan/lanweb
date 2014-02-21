# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.contrib.contenttypes.models import ContentType



class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ItemGroup'
        db.delete_table(u'logistic_itemgroup')

        # Deleting model 'Item'
        db.delete_table(u'logistic_item')
        for content_type in ContentType.objects.filter(app_label='myapp'):
            content_type.delete()


    def backwards(self, orm):
        # Adding model 'ItemGroup'
        db.create_table(u'logistic_itemgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'logistic', ['ItemGroup'])

        # Adding model 'Item'
        db.create_table(u'logistic_item', (
            ('product_model', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=150, blank=True)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('itemgroup', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['logistic.ItemGroup'])),
            ('holder', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='Holder', null=True, to=orm['userprofile.SiteUser'], blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'logistic', ['Item'])


    models = {
        
    }

    complete_apps = ['logistic']
