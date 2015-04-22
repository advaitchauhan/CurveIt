# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0007_auto_20150421_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='queryList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qlist', models.TextField(null=True)),
            ],
        ),
    ]
