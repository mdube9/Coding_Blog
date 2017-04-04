# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170318_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=120)),
                ('answer', models.TextField()),
                ('category', models.CharField(default='personal', max_length=120, choices=[('PERSONAL', 'personal'), ('CODING', 'coding'), ('WEB DEVELOPMENT', 'web development')])),
                ('updates', models.DateTimeField(auto_now=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
