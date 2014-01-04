# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crew'
        db.create_table(u'crew_crew', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'crew', ['Crew'])

        # Adding M2M table for field chief on 'Crew'
        m2m_table_name = db.shorten_name(u'crew_crew_chief')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crew', models.ForeignKey(orm[u'crew.crew'], null=False)),
            ('siteuser', models.ForeignKey(orm[u'userprofile.siteuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crew_id', 'siteuser_id'])

        # Adding model 'CrewTeam'
        db.create_table(u'crew_crewteam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crew.Crew'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.LanEvent'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'crew', ['CrewTeam'])

        # Adding M2M table for field members on 'CrewTeam'
        m2m_table_name = db.shorten_name(u'crew_crewteam_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crewteam', models.ForeignKey(orm[u'crew.crewteam'], null=False)),
            ('siteuser', models.ForeignKey(orm[u'userprofile.siteuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['crewteam_id', 'siteuser_id'])

        # Adding model 'Application'
        db.create_table(u'crew_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['userprofile.SiteUser'])),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('why', self.gf('django.db.models.fields.TextField')()),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('crew', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crew.CrewTeam'])),
            ('cv', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['event.LanEvent'])),
        ))
        db.send_create_signal(u'crew', ['Application'])


    def backwards(self, orm):
        # Deleting model 'Crew'
        db.delete_table(u'crew_crew')

        # Removing M2M table for field chief on 'Crew'
        db.delete_table(db.shorten_name(u'crew_crew_chief'))

        # Deleting model 'CrewTeam'
        db.delete_table(u'crew_crewteam')

        # Removing M2M table for field members on 'CrewTeam'
        db.delete_table(db.shorten_name(u'crew_crewteam_members'))

        # Deleting model 'Application'
        db.delete_table(u'crew_application')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'crew.application': {
            'Meta': {'object_name': 'Application'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'crew': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crew.CrewTeam']"}),
            'cv': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.LanEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userprofile.SiteUser']"}),
            'why': ('django.db.models.fields.TextField', [], {})
        },
        u'crew.crew': {
            'Meta': {'object_name': 'Crew'},
            'chief': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['userprofile.SiteUser']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'crew.crewteam': {
            'Meta': {'object_name': 'CrewTeam'},
            'crew': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crew.Crew']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['event.LanEvent']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['userprofile.SiteUser']", 'null': 'True', 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
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
        u'userprofile.siteuser': {
            'Meta': {'object_name': 'SiteUser'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '150', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'rfid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'steam': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['crew']