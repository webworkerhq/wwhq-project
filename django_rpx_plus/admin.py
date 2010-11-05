from django.contrib import admin
#from django.core.urlresolvers import reverse

from .models import RpxData

class RpxDataAdmin(admin.ModelAdmin):
    #NOTE: The 'profile' field is missing from the change form. Will add in the
    #      future.
    list_display = ('id', 'user', 'provider', 'identifier')
    list_display_links = ('id', 'provider', 'identifier')
admin.site.register(RpxData, RpxDataAdmin)
