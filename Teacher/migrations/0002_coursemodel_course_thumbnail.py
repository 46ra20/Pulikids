# Generated by Django 3.2.25 on 2025-02-11 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='course_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='Media/Thumbnail'),
        ),
    ]
