# Generated by Django 4.1.7 on 2023-04-05 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end',
        ),
    ]
