# Generated by Django 3.1.4 on 2020-12-24 05:00

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoeAvail', models.CharField(choices=[('In-stock', 'In Stock'), ('Sold-out', 'Sold Out'), ('Upcoming', 'Upcoming')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoeModel', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='shoe',
            old_name='brand',
            new_name='shoeModel',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='size',
        ),
        migrations.AddField(
            model_name='shoe',
            name='adminUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoe',
            name='image',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoe',
            name='releaseDate',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoe_size',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoe',
            name='brand_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shoes.brand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoeAvail',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shoes.stock'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoe',
            name='tags',
            field=models.ManyToManyField(to='shoes.Tag'),
        ),
    ]
