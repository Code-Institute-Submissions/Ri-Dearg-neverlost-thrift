# Generated by Django 3.0.7 on 2020-07-01 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20200701_0352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='original_bag',
            new_name='original_cart',
        ),
    ]
