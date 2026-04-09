from django.contrib import admin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "challenge", "created_at"]
    search_fields = ["name"]
    list_filter = ["challenge"]