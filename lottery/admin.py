from django.contrib import admin
# Register your models here.
from lottery.models import Female, Male

class FemaleAdmin(admin.ModelAdmin):
    list_display = ('identify','name','exchange_flag','sex')

class MaleAdmin(admin.ModelAdmin):
    list_display = ('identify','name','exchange_flag','sex')

admin.site.register(Female,FemaleAdmin)
admin.site.register(Male,MaleAdmin)
