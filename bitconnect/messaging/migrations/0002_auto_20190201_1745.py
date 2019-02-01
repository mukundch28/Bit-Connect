# Generated by Django 2.1.4 on 2019-02-01 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='members',
            field=models.ManyToManyField(related_name='conversations', related_query_name='members', to='base.Member'),
        ),
    ]