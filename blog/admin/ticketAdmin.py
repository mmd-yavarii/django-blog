from django.contrib import admin
from ..models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "phone", "created_at")
    list_display_links = ("subject",)
    search_fields = ("name", "email", "subject")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)