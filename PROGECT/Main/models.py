from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

# Table for storing all currencies and exchange rates.
class currency(models.Model):
    name_currency = models.CharField(max_length=255)
    value_name = models.CharField(max_length=255)
    value = models.FloatField()


# Table for storing currencies per year.
class annual_statistics(models.Model):
    name_currency2 = models.ForeignKey(currency, on_delete=models.CASCADE)
    year = models.DateTimeField()
    value = models.CharField(max_length=255)


# Table for storing messages.
class Message(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField(
        'Дата сообщения',
        default=timezone.now)


# Abstract model for storing the number of users.
class statistics(models.Model):
    statisticsUser = models.CharField(max_length=255, verbose_name='col_users')

    class Meta:
        abstract = True


# Model for storing the number of users and their names.
class statistics_users(statistics):
    name_user = models.CharField(max_length=255, verbose_name='name users')
