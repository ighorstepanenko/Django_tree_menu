# Generated by Django 4.1.7 on 2023-04-25 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='name',
            new_name='title',
        ),
    ]
