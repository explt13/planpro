# Generated by Django 4.2.6 on 2023-12-04 12:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0012_event_marker_id_event_popup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='recipient',
        ),
        migrations.AddField(
            model_name='event',
            name='recipient',
            field=models.ManyToManyField(related_name='recieved_events', to=settings.AUTH_USER_MODEL),
        ),
    ]
