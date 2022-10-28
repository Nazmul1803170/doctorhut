# Generated by Django 4.0.1 on 2022-05-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chember', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='forget_password',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_logout_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
