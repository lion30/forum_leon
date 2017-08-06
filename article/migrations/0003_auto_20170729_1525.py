# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-29 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(choices=[(0, '正常'), (1, '删除'), (10, '精华')], verbose_name='状态'),
        ),
    ]