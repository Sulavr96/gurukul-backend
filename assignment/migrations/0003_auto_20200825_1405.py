# Generated by Django 3.1 on 2020-08-25 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_assignment_resources'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='resources',
            new_name='resource',
        ),
    ]
