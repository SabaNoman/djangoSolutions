# Generated by Django 5.0.1 on 2024-02-08 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
    ]
