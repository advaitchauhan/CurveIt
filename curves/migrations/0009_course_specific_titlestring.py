# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0008_querylist'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_specific',
            name='titleString',
            field=models.CharField(default=b'blank', max_length=200),
        ),
    ]
