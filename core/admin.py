from django.contrib import admin
from core.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date_event", "date_create")
    list_filter = ('usuer', 'date_event',)
admin.site.register(Event, EventAdmin)
