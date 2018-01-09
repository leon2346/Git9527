# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='区域名称', max_length=50)),
                ('parent', models.ForeignKey(blank=True, to='app01.Area', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PicInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('path', models.ImageField(upload_to='app01')),
            ],
        ),
    ]
