# Generated by Django 2.1.4 on 2019-02-02 13:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_member_friend_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='last_seen',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 2, 13, 27, 42, 923371, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='member',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
