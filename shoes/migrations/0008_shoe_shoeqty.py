# Generated by Django 3.1.4 on 2021-05-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0007_auto_20201225_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='shoeQty',
            field=models.IntegerField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]