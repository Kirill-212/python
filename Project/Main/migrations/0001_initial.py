# Generated by Django 3.0.3 on 2020-03-10 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value_name', models.CharField(max_length=255)),
                ('value', models.FloatField()),
            ],
        ),
    ]
