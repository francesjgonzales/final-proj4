# Generated by Django 3.1.4 on 2020-12-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0004_auto_20201206_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='size',
            field=models.CharField(max_length=155),
        ),
    ]
