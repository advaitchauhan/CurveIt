# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0010_auto_20150429_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_specific',
            name='avg',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2),
        ),
    ]
