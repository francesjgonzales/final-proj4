# Generated by Django 3.1.4 on 2020-12-14 14:37

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0017_auto_20201213_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
