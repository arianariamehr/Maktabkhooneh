from django.contrib import admin
from blog.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["id", "author", "counted_views", "title", "status", "created_date", "updated_date",
                    "published_date"]
    list_filter = ["status", "author"]
    search_fields = ["title", "content"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["id", "name"]
    list_filter = ["name"]
    search_fields = ["name"]
