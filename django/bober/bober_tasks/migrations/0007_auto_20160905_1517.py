# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_tasks', '0006_auto_20160816_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='language',
            field=models.CharField(choices=[(b'sl', 'Slovenian'), (b'sr_Latn', 'Serbian'), (b'hr', 'Croatian'), (b'en', 'English'), (b'tr', 'Turkish')], max_length=8),
        ),
        migrations.AlterField(
            model_name='tasktranslation',
            name='language_locale',
            field=models.CharField(blank=True, choices=[(b'sl', 'Slovenian'), (b'sr_Latn', 'Serbian'), (b'hr', 'Croatian'), (b'en', 'English'), (b'tr', 'Turkish')], max_length=8, null=True),
        ),
    ]
