from django.contrib import admin

from .models import Service, Meeting

# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'meet_time', 'service', 'created_at']