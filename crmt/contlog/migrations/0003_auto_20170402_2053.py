# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contlog', '0002_auto_20170402_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['-id'], 'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.RemoveField(
            model_name='events',
            name='todate',
        ),
        migrations.AddField(
            model_name='events',
            name='reminder_date',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='дата напоминания'),
        ),
        migrations.AddField(
            model_name='events',
            name='spectacle_date',
            field=models.DateField(blank=True, db_index=True, null=True, verbose_name='дата спектакля'),
        ),
        migrations.AlterField(
            model_name='events',
            name='added',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='добавлено'),
        ),
    ]