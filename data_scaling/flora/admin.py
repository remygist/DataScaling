from django.contrib import admin

# Register your models here.
from .models import Plant, Discoverer

admin.site.register(Plant)
admin.site.register(Discoverer)