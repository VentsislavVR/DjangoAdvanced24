# Generated by Django 5.0.3 on 2024-03-06 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='USER',
            new_name='user',
        ),
    ]
