# Generated by Django 5.0.4 on 2024-05-03 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_user_follower_from_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='to_user',
            new_name='followers',
        ),
        migrations.RenameField(
            model_name='follower',
            old_name='from_user',
            new_name='user',
        ),
    ]