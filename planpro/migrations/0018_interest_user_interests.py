# Generated by Django 4.2.6 on 2024-01-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0017_alter_event_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(related_name='in_users_interests', to='planpro.interest'),
        ),
    ]
