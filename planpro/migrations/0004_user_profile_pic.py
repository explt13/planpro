# Generated by Django 4.2.6 on 2023-11-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planpro', '0003_remove_user_is_authenticated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]