# Generated by Django 3.1 on 2020-09-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurukul', '0007_auto_20200911_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructorrequest',
            name='resume',
            field=models.FileField(null=True, upload_to='gurukul/instructor_request/'),
        ),
    ]