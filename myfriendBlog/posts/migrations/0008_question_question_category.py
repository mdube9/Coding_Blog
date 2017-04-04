# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170318_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Question_Category',
            field=models.CharField(default='Arrays', max_length=120, choices=[('ARRAYS', 'Arrays'), ('STRINGS', 'Strings')]),
        ),
    ]
