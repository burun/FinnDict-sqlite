# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_word_times_practiced'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='next_practice',
            field=models.DateTimeField(default='', auto_now=True),
            preserve_default=False,
        ),
    ]
