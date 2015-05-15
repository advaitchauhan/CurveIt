# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0013_auto_20150503_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_specific',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='course_specific',
            name='prof',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='course_specific',
            name='titleString',
            field=models.CharField(default=b'blank', max_length=500),
        ),
    ]
