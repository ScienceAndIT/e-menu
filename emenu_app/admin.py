from django.contrib import admin
from emenu_app.models import Menu, Danie, Error


class DanieAdmin(admin.ModelAdmin):
    list_display = ('menu', 'title', 'description', 'picture')

admin.site.register(Menu)
admin.site.register(Danie, DanieAdmin)
admin.site.register(Error)
