from practicallyme.me.models import Page
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    list_display = ( 'owner', )

admin.site.register(Page, PageAdmin)
