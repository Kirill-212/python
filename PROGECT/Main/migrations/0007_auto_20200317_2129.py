# Generated by Django 3.0.4 on 2020-03-17 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20200317_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statistics_users',
            old_name='statistics_user',
            new_name='statisticsUser',
        ),
    ]
