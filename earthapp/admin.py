from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from earthapp.models import Earthapp
admin.site.register(Earthapp, DraggableMPTTAdmin)
