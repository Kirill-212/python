# Generated by Django 3.0.4 on 2020-03-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_auto_20200317_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics_users',
            name='statisticsUser',
            field=models.CharField(max_length=255, verbose_name='col_users'),
        ),
    ]
