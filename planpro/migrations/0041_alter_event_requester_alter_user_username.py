# Generated by Django 4.2.6 on 2024-01-12 12:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0040_alter_event_initial_recipients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='requester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-z]*$', 'Only lower alphanumeric characters are allowed for the username.')]),
        ),
    ]