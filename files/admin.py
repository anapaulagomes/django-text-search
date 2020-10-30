from django.contrib import admin

from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_display = ("url",)
