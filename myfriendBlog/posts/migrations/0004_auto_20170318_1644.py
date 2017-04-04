# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='personal', max_length=120, choices=[('PERSONAL', 'personal'), ('CODING', 'coding'), ('WEB DEVELOPMENT', 'web development')]),
        ),
    ]
