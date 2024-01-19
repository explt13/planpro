# Generated by Django 4.2.6 on 2024-01-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0024_mail_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(),
        ),
    ]