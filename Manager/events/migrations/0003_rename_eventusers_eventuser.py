# Generated by Django 4.2.6 on 2023-10-15 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_user_eventusers_rename_adress_venue_address_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventUsers',
            new_name='EventUser',
        ),
    ]