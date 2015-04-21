# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0006_auto_20150416_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('netid', models.CharField(max_length=50)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('year', models.CharField(default=b'', max_length=4)),
                ('has_Entered', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
