# Generated by Django 4.2.6 on 2023-11-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_venue_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]