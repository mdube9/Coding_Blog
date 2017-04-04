# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='spcomplex',
            field=models.CharField(default='O(1)', max_length=12),
        ),
        migrations.AddField(
            model_name='question',
            name='ticomplex',
            field=models.CharField(default='O(n^2)', max_length=12),
        ),
    ]
