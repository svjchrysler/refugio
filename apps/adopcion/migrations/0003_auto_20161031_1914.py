# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 23:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0002_solicitud'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='appelido',
            new_name='apellidos',
        ),
    ]
