from django.contrib import admin
from website.models import Contact, Newsletter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["name", "subject", "email", "created_date", "updated_date"]
    list_filter = ["email"]
    search_fields = ["name", "subject", "message"]


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["email"]
    list_filter = ["email"]
    search_fields = ["email"]
