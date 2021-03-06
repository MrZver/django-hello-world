# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User1'
        db.create_table('user_table', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date_of_birth', self.gf('django.db.models.fields.DateTimeField')()),
            ('bio', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=30)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(max_length=300)),
        ))
        db.send_create_signal(u'app', ['User1'])


    def backwards(self, orm):
        # Deleting model 'User1'
        db.delete_table('user_table')


    models = {
        u'app.user1': {
            'Meta': {'object_name': 'User1', 'db_table': "'user_table'"},
            'bio': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '30'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['app']