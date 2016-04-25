# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-25 13:23
from __future__ import unicode_literals

from django.db import migrations
import post_office.validators
import tinymce_4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post_office', '0003_longer_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='html_message',
            field=tinymce_4.fields.TinyMCEModelDefaultField(blank=True, verbose_name='HTML Message'),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='html_content',
            field=tinymce_4.fields.TinyMCEModelDefaultField(blank=True, validators=[post_office.validators.validate_template_syntax], verbose_name='HTML content'),
        ),
    ]
