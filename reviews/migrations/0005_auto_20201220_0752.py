# Generated by Django 3.1.4 on 2020-12-20 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20201220_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='price',
        ),
        migrations.RemoveField(
            model_name='review',
            name='shoeModel',
        ),
    ]