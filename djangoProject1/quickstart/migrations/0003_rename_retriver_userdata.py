# Generated by Django 5.1.5 on 2025-02-04 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_alter_retriver_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Retriver',
            new_name='UserData',
        ),
    ]
