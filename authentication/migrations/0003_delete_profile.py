# Generated by Django 4.1.3 on 2022-12-06 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]