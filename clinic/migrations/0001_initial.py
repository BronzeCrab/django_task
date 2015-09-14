# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year_in_school', models.CharField(default=b'Viktorova', max_length=2, choices=[(b'Viktorova', b'Viktorova'), (b'Ivanova', b'Ivanova')])),
                ('doc_name', models.CharField(max_length=200)),
                ('visit_date', models.DateTimeField(verbose_name=b'date of the visit')),
                ('visit_time', models.DateTimeField(verbose_name=b'time of the visit')),
                ('client_name', models.CharField(max_length=200)),
            ],
        ),
    ]
