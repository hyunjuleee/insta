# Generated by Django 4.2.15 on 2024-08-12 06:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_followings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
