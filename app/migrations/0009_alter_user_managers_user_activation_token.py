# Generated by Django 4.0 on 2023-07-18 04:03

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_user_accept_terms_user_apartment_suite_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='activation_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]