# Generated by Django 4.1.7 on 2023-04-05 12:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]