# Generated by Django 2.0.13 on 2020-01-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(default='TestVideo', max_length=500),
        ),
    ]
