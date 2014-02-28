# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'booker_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'booker', ['Customer'])

        # Adding model 'Book'
        db.create_table(u'booker_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'booker', ['Book'])

        # Adding M2M table for field customer on 'Book'
        m2m_table_name = db.shorten_name(u'booker_book_customer')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm[u'booker.book'], null=False)),
            ('customer', models.ForeignKey(orm[u'booker.customer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['book_id', 'customer_id'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'booker_customer')

        # Deleting model 'Book'
        db.delete_table(u'booker_book')

        # Removing M2M table for field customer on 'Book'
        db.delete_table(db.shorten_name(u'booker_book_customer'))


    models = {
        u'booker.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'customer': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['booker.Customer']", 'symmetrical': 'False'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'booker.customer': {
            'Meta': {'object_name': 'Customer'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['booker']