# Generated by Django 4.2.6 on 2023-12-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='category',
            field=models.CharField(choices=[('friends', 'Friends'), ('events', 'Events')], default='null', max_length=20),
            preserve_default=False,
        ),
    ]
