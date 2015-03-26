# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Specific',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dept', models.CharField(max_length=3)),
                ('num', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=100)),
                ('prof', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=11)),
                ('num_A_plus', models.IntegerField(default=0)),
                ('num_A', models.IntegerField(default=0)),
                ('num_A_minus', models.IntegerField(default=0)),
                ('num_B_plus', models.IntegerField(default=0)),
                ('num_B', models.IntegerField(default=0)),
                ('num_B_minus', models.IntegerField(default=0)),
                ('num_C_plus', models.IntegerField(default=0)),
                ('num_C', models.IntegerField(default=0)),
                ('num_C_minus', models.IntegerField(default=0)),
                ('num_D_grade', models.IntegerField(default=0)),
                ('num_F_grade', models.IntegerField(default=0)),
                ('num_D_pass_fail', models.IntegerField(default=0)),
                ('num_F_pass_fail', models.IntegerField(default=0)),
                ('num_P_pass_fail', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('netid', models.CharField(max_length=20)),
                ('has_Entered', models.BooleanField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
