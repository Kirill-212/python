from django.contrib import admin

from .models import currency, Message, annual_statistics, statistics_users

# Register your models here.

# Adding tables for correction.
admin.site.register(currency)
admin.site.register(Message)
admin.site.register(annual_statistics)
admin.site.register(statistics_users)
