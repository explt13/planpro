# Generated by Django 4.2.6 on 2023-12-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0011_user_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
