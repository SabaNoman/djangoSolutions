# Generated by Django 5.0.1 on 2024-02-08 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_review_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_name',
            new_name='username',
        ),
    ]
