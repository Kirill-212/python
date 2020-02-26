# Generated by Django 3.0.3 on 2020-02-25 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Riddle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riddle_text', models.CharField(max_length=255)),
                ('pub_date', models.DateField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
                ('riddle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.Riddle')),
            ],
        ),
    ]
