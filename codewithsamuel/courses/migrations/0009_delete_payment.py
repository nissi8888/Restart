# Generated by Django 5.0.1 on 2024-02-15 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_usercourse_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
