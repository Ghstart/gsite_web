# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gApi', '0004_auto_20170609_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobbole_detail_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_description_content', models.TextField(verbose_name='详细的自我描述')),
                ('detail_info_url', models.URLField(max_length=300, verbose_name='详情链接')),
                ('detail_info_url_object_id', models.CharField(max_length=50, verbose_name='链接的加密')),
                ('images_url_datas', models.CharField(max_length=300, verbose_name='妹子发的图片集')),
            ],
            options={
                'verbose_name': '相亲详细信息',
                'verbose_name_plural': '相亲详细信息',
            },
        ),
        migrations.CreateModel(
            name='jobbole_image_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_info_url', models.URLField(max_length=300, verbose_name='详情链接')),
                ('detail_info_url_object_id', models.CharField(max_length=50, verbose_name='链接的加密')),
                ('image_url', models.CharField(max_length=300, verbose_name='妹子发的单张图片')),
            ],
            options={
                'verbose_name': '相亲图片信息',
                'verbose_name_plural': '相亲图片信息',
            },
        ),
    ]
