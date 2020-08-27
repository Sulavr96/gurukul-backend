# Generated by Django 3.1 on 2020-08-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurukul', '0003_auto_20200825_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='username',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_image/'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_image_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
