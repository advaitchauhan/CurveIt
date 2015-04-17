# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0002_auto_20150325_1439'),
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
        migrations.AlterField(
            model_name='course_specific',
            name='dept',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course_specific',
            name='num',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course_specific',
            name='prof',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course_specific',
            name='semester',
            field=models.CharField(max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='netid',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
