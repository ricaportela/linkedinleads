from django.contrib import admin
from leadsapp.models import Linkedinleads

# Register your models here.


class LinkedinleadsAdmin(admin.ModelAdmin):
    fieldsets= [
        ('id', {'fields': ['id']}),
        ('name', {'fields': ['name']}),
        ('link', {'fields': ['link']}),
        ('dateinvite', {'fields': ['dateinvite']}),
        
    ]
    list_display = ('id', 'name', 'dateinvite')
    list_filter = ['name']
    

admin.site.register(Linkedinleads, LinkedinleadsAdmin)