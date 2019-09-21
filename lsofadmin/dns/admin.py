from .models import Record, Domain

from django.contrib import admin

class DomainAdmin(admin.ModelAdmin):
    search_fields = ['name']

class RecordAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ip_address']

admin.site.register(Record, RecordAdmin)
admin.site.register(Domain, DomainAdmin)