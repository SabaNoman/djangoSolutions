# Generated by Django 5.0.1 on 2024-02-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_orderdetails_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]
