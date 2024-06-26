# Generated by Django 4.2.6 on 2024-01-17 10:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0054_remove_event_archived_user_event_archived_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-z]*$', 'Only lower alphanumeric characters are allowed for the username.'), django.core.validators.MinLengthValidator(3, 'Username must be at least 3 characters')]),
        ),
    ]
