# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0005_auto_20150415_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_specific',
            name='name',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course_specific',
            name='prof',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
