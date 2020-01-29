from django.contrib import admin
from .models import Department, Level, Material, Faculty

# Register your models here.
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Material)
admin.site.register(Faculty)
