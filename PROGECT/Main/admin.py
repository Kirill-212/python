from django.contrib import admin

from .models import  currency,Message,annual_statistics

# Register your models here.

admin.site.register(currency)
admin.site.register(Message)
admin.site.register(annual_statistics)
