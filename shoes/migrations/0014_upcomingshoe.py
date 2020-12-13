# Generated by Django 3.1.4 on 2020-12-08 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0013_shoe_shoebrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingShoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoeModel', models.CharField(max_length=255)),
                ('shoeBrand', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('color', models.CharField(max_length=155)),
                ('releaseDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('shoeAvail', models.CharField(choices=[('In-stock', 'In Stock'), ('Sold-out', 'Sold Out'), ('Coming-Soon', 'Coming Soon')], max_length=11)),
            ],
        ),
    ]