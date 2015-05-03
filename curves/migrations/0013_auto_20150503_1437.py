# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0012_auto_20150430_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_specific',
            name='semester',
            field=models.CharField(max_length=11),
        ),
    ]
