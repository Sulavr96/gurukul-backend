# Generated by Django 3.1 on 2020-08-28 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gurukul', '0004_auto_20200827_0520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['first_name']},
        ),
    ]
