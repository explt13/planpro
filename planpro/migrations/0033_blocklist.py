# Generated by Django 4.2.6 on 2024-01-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0032_alter_mail_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blocklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.GenericIPAddressField()),
            ],
        ),
    ]
