# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('locu_id', models.CharField(max_length=250, null=True, blank=True)),
                ('foursquare_id', models.CharField(max_length=250, null=True, blank=True)),
            ],
        ),
    ]
