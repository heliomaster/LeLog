# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LogBook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logfields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_field', models.DateTimeField()),
                ('off_block_time', models.TimeField()),
                ('take_off_time', models.TimeField()),
                ('on_block_time', models.TimeField()),
                ('tot_time_field', models.TimeField()),
                ('pic_field', models.CharField(max_length=50)),
                ('fo_field', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mycsvmodel',
            name='conditions',
            field=models.CharField(choices=[('D', 'Day'), ('N', 'Night')], default='?', max_length=1),
        ),
        migrations.AddField(
            model_name='mycsvmodel',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='logfields',
            name='arrival_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_field', to='LogBook.MycsvModel'),
        ),
        migrations.AddField(
            model_name='logfields',
            name='dep_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dep_field', to='LogBook.MycsvModel'),
        ),
    ]
