# Generated by Django 4.2.6 on 2024-01-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0034_delete_blocklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event_recipient',
            name='is_accepted',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTE', 'Accepted'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20),
        ),
    ]