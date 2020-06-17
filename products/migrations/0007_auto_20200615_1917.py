# Generated by Django 3.0.7 on 2020-06-15 17:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200608_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockDrop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='stock_drop')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_drop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.StockDrop'),
        ),
    ]