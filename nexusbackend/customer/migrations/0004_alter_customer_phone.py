# Generated by Django 4.2.5 on 2023-09-10 14:30

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+1234567890', max_length=128, region=None, unique=True),
        ),
    ]