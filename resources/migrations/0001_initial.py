# Generated by Django 3.1 on 2020-08-27 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0004_auto_20200827_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('content', models.FileField(blank=True, upload_to='resources/resource/')),
                ('resource_url', models.CharField(blank=True, max_length=500)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='course.course')),
            ],
        ),
    ]
