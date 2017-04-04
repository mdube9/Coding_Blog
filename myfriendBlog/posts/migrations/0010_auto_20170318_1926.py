# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_question_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(choices=[('Concept Done', '1_Concept_Done'), ('Code', '2_Code'), ('Done', '3_Done')], default='Thinking.', max_length=120),
        ),
    ]
