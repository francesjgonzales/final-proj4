# Generated by Django 3.1.4 on 2020-12-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0006_auto_20201225_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
