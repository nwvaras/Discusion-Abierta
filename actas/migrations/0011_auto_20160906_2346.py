# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actas', '0010_encuentro_hash_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuentro',
            name='hash_search',
            field=models.UUIDField(default=b'3b66133074a511e6b72f40e230d28fea'),
        ),
    ]