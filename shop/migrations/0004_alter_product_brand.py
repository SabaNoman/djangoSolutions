# Generated by Django 5.0.1 on 2024-02-07 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.brand'),
        ),
    ]
