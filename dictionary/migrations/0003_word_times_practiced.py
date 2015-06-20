# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_word_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='times_practiced',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
    ]
