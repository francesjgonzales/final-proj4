# Generated by Django 3.1.4 on 2020-12-24 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_auto_20201224_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='price',
        ),
    ]
