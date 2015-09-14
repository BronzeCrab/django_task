# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='year_in_school',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doc_name',
            field=models.CharField(default=b'Viktorova', max_length=2, choices=[(b'Viktorova', b'Viktorova'), (b'Ivanova', b'Ivanova')]),
        ),
    ]
