# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20170318_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='spcomplex',
            new_name='space_complexity',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='ticomplex',
            new_name='time_complexity',
        ),
    ]
