# Generated by Django 3.2.7 on 2022-09-29 19:52

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+911122334455', max_length=128, region=None, verbose_name='Phone Number'),
        ),
    ]
