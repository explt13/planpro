# Generated by Django 4.2.6 on 2024-01-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0026_rename_time_mail_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(),
        ),
    ]