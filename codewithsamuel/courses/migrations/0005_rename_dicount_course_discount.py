# Generated by Django 5.0.2 on 2024-02-11 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_video_video_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='dicount',
            new_name='discount',
        ),
    ]