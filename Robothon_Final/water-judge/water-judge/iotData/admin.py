from django.contrib import admin
from .models import Sensor, Reading
admin.site.register(Sensor)
admin.site.register(Reading)
# Register your models here.
