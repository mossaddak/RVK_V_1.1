# Generated by Django 4.1.7 on 2023-04-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Volunteer Description',
            },
        ),
    ]