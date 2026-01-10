from django.contrib import admin
from .models import Building, Room, Computer

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'building', 'width', 'height')

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'pc_name', 'status', 'room')
