from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Room)
admin.site.register(Sdet)
admin.site.register(Message)
admin.site.register(Topic)