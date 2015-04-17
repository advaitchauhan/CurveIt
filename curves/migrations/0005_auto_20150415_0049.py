# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0004_auto_20150415_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.CharField(default=b'', max_length=4),
            preserve_default=True,
        ),
    ]
