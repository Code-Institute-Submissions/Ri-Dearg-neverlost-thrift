# Generated by Django 3.0.7 on 2020-06-06 00:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='user_tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), blank=True, default=list, size=7),
        ),
    ]