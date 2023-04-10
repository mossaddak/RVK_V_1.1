# Generated by Django 4.1.7 on 2023-04-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiative', '0006_peaceeducationprogramandeducationfirstsection_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='peaceeducationprogramandeducationfirstsection',
            name='category',
            field=models.CharField(choices=[('Humanitarian', 'Humanitarian'), ('Peace Education Program', 'Peace Education Program'), ('Peace Education & Knowledge', 'Peace Education & Knowledge')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='peaceeducationprogramfourthsection',
            name='category',
            field=models.CharField(choices=[('Humanitarian', 'Humanitarian'), ('Peace Education Program', 'Peace Education Program'), ('Peace Education & Knowledge', 'Peace Education & Knowledge')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='peaceeducationprogramsecondsection',
            name='category',
            field=models.CharField(choices=[('Humanitarian', 'Humanitarian'), ('Peace Education Program', 'Peace Education Program'), ('Peace Education & Knowledge', 'Peace Education & Knowledge')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='peaceeducationprogramthiredsection',
            name='category',
            field=models.CharField(choices=[('Humanitarian', 'Humanitarian'), ('Peace Education Program', 'Peace Education Program'), ('Peace Education & Knowledge', 'Peace Education & Knowledge')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='peaceeducationprogramtopsection',
            name='category',
            field=models.CharField(choices=[('Humanitarian', 'Humanitarian'), ('Peace Education Program', 'Peace Education Program'), ('Peace Education & Knowledge', 'Peace Education & Knowledge')], max_length=50, null=True),
        ),
    ]