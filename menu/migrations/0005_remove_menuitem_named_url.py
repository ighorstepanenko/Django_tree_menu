# Generated by Django 4.1.7 on 2023-04-28 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menuitem_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='named_url',
        ),
    ]
