# Generated by Django 2.1 on 2018-10-02 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bober_simple_competition', '0058_auto_20180828_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='remote_addr',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
