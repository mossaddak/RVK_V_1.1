# Generated by Django 4.1.7 on 2023-04-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestvideo',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='latestvideo',
            name='link',
            field=models.CharField(max_length=350, null=True, verbose_name='Video Playlist Link'),
        ),
    ]