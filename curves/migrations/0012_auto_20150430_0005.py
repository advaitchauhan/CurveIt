# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0011_auto_20150429_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_specific',
            old_name='num_D_PDF',
            new_name='num_D',
        ),
        migrations.RenameField(
            model_name='course_specific',
            old_name='num_D_grade',
            new_name='num_F',
        ),
        migrations.RenameField(
            model_name='course_specific',
            old_name='num_F_PDF',
            new_name='num_P',
        ),
        migrations.RemoveField(
            model_name='course_specific',
            name='num_F_grade',
        ),
        migrations.RemoveField(
            model_name='course_specific',
            name='num_P_PDF',
        ),
    ]
