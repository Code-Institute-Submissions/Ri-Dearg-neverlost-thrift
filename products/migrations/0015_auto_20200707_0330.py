# Generated by Django 3.0.7 on 2020-07-07 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_in_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_stock',
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
    ]
