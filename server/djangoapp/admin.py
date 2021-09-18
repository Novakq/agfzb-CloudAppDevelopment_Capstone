from django.contrib import admin
# from .models import related models

from .models import *

admin.site.register(CarMake)
admin.site.register(CarModel)

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel 
    extra = 5

# CarModelAdmin class

class CarModelAdminInline(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    
    inlines = [CarModelInline]


# Register models here
