# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-20 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_paper_submissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juniordefaultyear',
            name='school_category',
            field=models.CharField(choices=[('ELEMENTARY', 'Elementary school'), ('HIGHSCHOOL', 'High school'), ('KINDERGARDEN', 'Kindergarden')], max_length=24),
        ),
    ]
