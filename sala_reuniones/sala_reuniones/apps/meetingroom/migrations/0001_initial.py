# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-25 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('state', '0001_initial'),
        ('supply', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('capacity', models.IntegerField()),
                ('availability_schedule', models.DateTimeField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_meetingroom', to='state.State')),
                ('supplies', models.ManyToManyField(to='supply.Supply')),
            ],
        ),
    ]