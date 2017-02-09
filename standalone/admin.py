from django.contrib import admin

from .models import StandAlone


@admin.register(StandAlone)
class StandAloneAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
