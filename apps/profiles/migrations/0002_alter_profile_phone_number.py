# Generated by Django 3.2.7 on 2022-09-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(default='+911122334455', verbose_name='Phone Number'),
        ),
    ]