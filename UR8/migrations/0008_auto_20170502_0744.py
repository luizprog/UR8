# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UR8', '0007_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos'),
        ),
    ]