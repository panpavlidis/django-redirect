# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-14 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_url', models.CharField(db_index=True, help_text="Absolute path, excluding the domain. Example: '/about/'", max_length=255, unique=True, verbose_name='From URL')),
                ('to_url', models.CharField(db_index=True, help_text='Absolute path or full domain. Example: http://www.example.com', max_length=255, verbose_name='To URL')),
                ('http_status', models.SmallIntegerField(choices=[(301, '301 - Permanent Redirect'), (302, '302 - Temporary Redirect')], default=301, verbose_name='HTTP Status')),
                ('status', models.BooleanField(choices=[(True, 'Active'), (False, 'Inactive')], default=True)),
                ('uses_regex', models.BooleanField(default=False, help_text='Check if the From URL uses a regular expression. If so, it will be moved to the top the URL patterns and processed first', verbose_name='Uses Regular Expression')),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('update_dt', models.DateTimeField(auto_now=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'ordering': ('-uses_regex',),
                'verbose_name': 'redirect',
                'verbose_name_plural': 'redirects',
            },
        ),
        migrations.AlterUniqueTogether(
            name='redirect',
            unique_together=set([('site', 'from_url')]),
        ),
    ]