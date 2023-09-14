# Generated by Django 4.2.5 on 2023-09-10 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='country',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='location',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]