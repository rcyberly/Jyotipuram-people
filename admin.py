from django.contrib import admin
from Jpeople.models import Jpeople
class JpeopleAdmin(admin.ModelAdmin):
    list_display = ('yourtext','fileup')
admin.site.register(Jpeople,JpeopleAdmin)


# Register your models here.
