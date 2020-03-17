from django.contrib import admin
from .models import Option, Riddle,Message

# Register your models here.


admin.site.register(Riddle)
admin.site.register(Option)
admin.site.register(Message)