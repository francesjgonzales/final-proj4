# Generated by Django 3.1.4 on 2021-05-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0008_shoe_shoeqty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='shoeQty',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]