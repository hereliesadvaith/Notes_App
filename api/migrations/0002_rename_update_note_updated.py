# Generated by Django 4.2 on 2023-04-29 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='update',
            new_name='updated',
        ),
    ]
