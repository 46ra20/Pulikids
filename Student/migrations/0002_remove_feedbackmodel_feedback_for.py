# Generated by Django 3.2.25 on 2025-02-11 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackmodel',
            name='feedback_for',
        ),
    ]
