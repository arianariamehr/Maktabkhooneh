from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["id", "author", "title", "counted_views", "status", "created_date", "updated_date",
                    "published_date"]
    list_filter = ["status", "author"]
    search_fields = ["title", "excert", "content"]
