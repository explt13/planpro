# Generated by Django 4.2.6 on 2024-01-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0018_interest_user_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(blank=True, null=True, related_name='in_users_interests', to='planpro.interest'),
        ),
    ]
