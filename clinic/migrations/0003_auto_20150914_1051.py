# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_auto_20150914_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='visit_date',
            field=models.DateField(verbose_name=b'date of the visit'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='visit_time',
            field=models.TimeField(verbose_name=b'time of the visit'),
        ),
    ]
