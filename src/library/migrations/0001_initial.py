# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Anime'
        db.create_table(u'library_anime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('synopsis', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['Anime'])

        # Adding M2M table for field genres on 'Anime'
        m2m_table_name = db.shorten_name(u'library_anime_genres')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('anime', models.ForeignKey(orm[u'library.anime'], null=False)),
            ('genre', models.ForeignKey(orm[u'library.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['anime_id', 'genre_id'])

        # Adding M2M table for field demographics on 'Anime'
        m2m_table_name = db.shorten_name(u'library_anime_demographics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('anime', models.ForeignKey(orm[u'library.anime'], null=False)),
            ('demographic', models.ForeignKey(orm[u'library.demographic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['anime_id', 'demographic_id'])

        # Adding M2M table for field alternative_titles on 'Anime'
        m2m_table_name = db.shorten_name(u'library_anime_alternative_titles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('anime', models.ForeignKey(orm[u'library.anime'], null=False)),
            ('title', models.ForeignKey(orm[u'library.title'], null=False))
        ))
        db.create_unique(m2m_table_name, ['anime_id', 'title_id'])

        # Adding model 'Title'
        db.create_table(u'library_title', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'library', ['Title'])

        # Adding model 'Serie'
        db.create_table(u'library_serie', (
            (u'anime_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.Anime'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'library', ['Serie'])

        # Adding M2M table for field episodes on 'Serie'
        m2m_table_name = db.shorten_name(u'library_serie_episodes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('serie', models.ForeignKey(orm[u'library.serie'], null=False)),
            ('episode', models.ForeignKey(orm[u'library.episode'], null=False))
        ))
        db.create_unique(m2m_table_name, ['serie_id', 'episode_id'])

        # Adding model 'Episode'
        db.create_table(u'library_episode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('synopsis', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('date_aired', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['Episode'])

        # Adding model 'Movie'
        db.create_table(u'library_movie', (
            (u'anime_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.Anime'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'library', ['Movie'])

        # Adding model 'OAD'
        db.create_table(u'library_oad', (
            (u'anime_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.Anime'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'library', ['OAD'])

        # Adding model 'Genre'
        db.create_table(u'library_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['Genre'])

        # Adding model 'Demographic'
        db.create_table(u'library_demographic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'library', ['Demographic'])

        # Adding model 'Tag'
        db.create_table(u'library_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'library', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Anime'
        db.delete_table(u'library_anime')

        # Removing M2M table for field genres on 'Anime'
        db.delete_table(db.shorten_name(u'library_anime_genres'))

        # Removing M2M table for field demographics on 'Anime'
        db.delete_table(db.shorten_name(u'library_anime_demographics'))

        # Removing M2M table for field alternative_titles on 'Anime'
        db.delete_table(db.shorten_name(u'library_anime_alternative_titles'))

        # Deleting model 'Title'
        db.delete_table(u'library_title')

        # Deleting model 'Serie'
        db.delete_table(u'library_serie')

        # Removing M2M table for field episodes on 'Serie'
        db.delete_table(db.shorten_name(u'library_serie_episodes'))

        # Deleting model 'Episode'
        db.delete_table(u'library_episode')

        # Deleting model 'Movie'
        db.delete_table(u'library_movie')

        # Deleting model 'OAD'
        db.delete_table(u'library_oad')

        # Deleting model 'Genre'
        db.delete_table(u'library_genre')

        # Deleting model 'Demographic'
        db.delete_table(u'library_demographic')

        # Deleting model 'Tag'
        db.delete_table(u'library_tag')


    models = {
        u'library.anime': {
            'Meta': {'object_name': 'Anime'},
            'alternative_titles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Title']", 'symmetrical': 'False'}),
            'demographics': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Demographic']", 'symmetrical': 'False'}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Genre']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'synopsis': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'library.demographic': {
            'Meta': {'object_name': 'Demographic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'library.episode': {
            'Meta': {'object_name': 'Episode'},
            'date_aired': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'synopsis': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'library.genre': {
            'Meta': {'object_name': 'Genre'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'library.movie': {
            'Meta': {'object_name': 'Movie', '_ormbases': [u'library.Anime']},
            u'anime_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['library.Anime']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'library.oad': {
            'Meta': {'object_name': 'OAD', '_ormbases': [u'library.Anime']},
            u'anime_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['library.Anime']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'library.serie': {
            'Meta': {'object_name': 'Serie', '_ormbases': [u'library.Anime']},
            u'anime_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['library.Anime']", 'unique': 'True', 'primary_key': 'True'}),
            'episodes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Episode']", 'symmetrical': 'False'})
        },
        u'library.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'library.title': {
            'Meta': {'object_name': 'Title'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['library']