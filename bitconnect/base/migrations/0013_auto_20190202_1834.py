# Generated by Django 2.1.4 on 2019-02-02 18:34

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20190202_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=base.models.path_and_rename),
        ),
    ]
