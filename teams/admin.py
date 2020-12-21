from django.contrib import admin

# Register your models here.
from teams.models import Coach, School, Team

admin.site.register(Coach)
admin.site.register(School)
admin.site.register(Team)
