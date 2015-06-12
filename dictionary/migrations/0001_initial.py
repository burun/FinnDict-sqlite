# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('finnish', models.CharField(unique=True, max_length=128)),
                ('english', models.CharField(max_length=128)),
                ('chinese', models.CharField(max_length=128, blank=True)),
                ('sentence', models.CharField(max_length=256, blank=True)),
                ('note', models.CharField(max_length=256, blank=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
