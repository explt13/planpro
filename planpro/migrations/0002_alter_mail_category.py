# Generated by Django 4.2.6 on 2023-12-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='category',
            field=models.CharField(choices=[('FRIENDS', 'Friends'), ('EVENTS', 'Events')], max_length=20),
        ),
    ]
