# Generated by Django 5.0.1 on 2024-02-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_rename_created_at_review_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]