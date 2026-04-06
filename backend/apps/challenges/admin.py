from django.contrib import admin
from .models import Challenge


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "start_date", "end_date", "created_at"]
    search_fields = ["name"]