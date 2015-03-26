# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_specific',
            old_name='num_D_pass_fail',
            new_name='num_D_PDF',
        ),
        migrations.RenameField(
            model_name='course_specific',
            old_name='num_F_pass_fail',
            new_name='num_F_PDF',
        ),
        migrations.RenameField(
            model_name='course_specific',
            old_name='num_P_pass_fail',
            new_name='num_P_PDF',
        ),
    ]
