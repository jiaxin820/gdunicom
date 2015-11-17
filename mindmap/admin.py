from django.contrib import admin
from .models import MapDetail

class MapAdmin(admin.ModelAdmin):
	pass

admin.site.register(MapDetail,MapAdmin)
