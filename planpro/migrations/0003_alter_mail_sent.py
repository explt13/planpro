# Generated by Django 4.2.6 on 2023-12-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0002_mail_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='sent',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
