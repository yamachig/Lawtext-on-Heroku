from django.contrib import admin

from file_server.models import File

class FileAdmin(admin.ModelAdmin):
    pass
admin.site.register(File, FileAdmin)
