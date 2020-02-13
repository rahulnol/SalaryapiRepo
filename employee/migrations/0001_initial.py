# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-12 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.CharField(default=6951, editable=False, max_length=4, unique=True)),
                ('hiredate', models.DateField()),
                ('pfno', models.PositiveIntegerField()),
                ('probation_period', models.CharField(choices=[('1month', '1 Month'), ('2month', '2 Month'), ('3month', '3 Month')], max_length=100)),
            ],
        ),
    ]