# Generated by Django 4.1.3 on 2022-12-10 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_alter_profile_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='dates_to_pull',
            new_name='weights_to_pull',
        ),
    ]