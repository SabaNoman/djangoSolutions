# Generated by Django 4.2.9 on 2024-02-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_product_name_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='True', default='', max_length=50)),
            ],
        ),
    ]