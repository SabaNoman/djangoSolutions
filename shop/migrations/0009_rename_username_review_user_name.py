# Generated by Django 5.0.1 on 2024-02-08 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_rename_user_name_review_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='username',
            new_name='user_name',
        ),
    ]
