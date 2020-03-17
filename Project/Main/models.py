from django.db import models


# Create your models here.


class currency(models.Model):
    name = models.CharField(max_length=255)
    value_name = models.CharField(max_length=255)
    value = models.FloatField()
