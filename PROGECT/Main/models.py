from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class currency(models.Model):
    name_currency = models.CharField(max_length=255)
    value_name = models.CharField(max_length=255)
    value = models.FloatField()


class annual_statistics(models.Model):
    name_currency2 = models.ForeignKey(currency, on_delete=models.CASCADE)
    year = models.DateTimeField()
    value = models.CharField(max_length=255)


class Message(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)


class statistics(models.Model):
    statisticsUser = models.CharField(max_length=255, verbose_name='col_users')

    class Meta:
        abstract = True


class statistics_users(statistics):
    name_user = models.CharField(max_length=255, verbose_name='name users')


