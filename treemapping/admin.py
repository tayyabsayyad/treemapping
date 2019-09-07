from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis import admin

from .models import TreeData


@admin.register(TreeData)
class TreeAdmin(OSMGeoAdmin):
    list_display = ('location', 'city')
