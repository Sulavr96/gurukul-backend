# Generated by Django 3.1 on 2020-09-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurukul', '0008_instructorrequest_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructorrequest',
            name='resume_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
