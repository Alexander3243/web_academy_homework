# Generated by Django 4.1.3 on 2023-01-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extension_users', '0003_user_address_user_city_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
    ]
