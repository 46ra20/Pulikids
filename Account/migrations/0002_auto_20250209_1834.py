# Generated by Django 3.2.25 on 2025-02-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistrationmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Media/Account'),
        ),
        migrations.AlterField(
            model_name='teacherregistrationmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Media/Account'),
        ),
    ]
