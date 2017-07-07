from django.contrib import admin

from sample.models import Car


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year']
    filter_horizontal = ['tags',]


admin.site.register(Car, CarAdmin)