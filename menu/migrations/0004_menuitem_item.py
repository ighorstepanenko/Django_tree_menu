# Generated by Django 4.1.7 on 2023-04-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_menuitem_is_active_menuitem_named_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='item',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
    ]