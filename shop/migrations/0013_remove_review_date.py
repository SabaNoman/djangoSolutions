# Generated by Django 5.0.1 on 2024-02-10 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_review_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='date',
        ),
    ]
