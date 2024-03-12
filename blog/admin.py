from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["id", "avatar_image", "title", "status", "login_require", "created_date", "updated_date",
                    "published_date"]
    list_filter = ["status", "author"]
    search_fields = ["title", "content"]
    summernote_fields = ["content"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["id", "name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ["id", "name", "subject", "created_date", "updated_date", "approved"]
    list_filter = ["name", "post", "approved"]
    search_fields = ["subject", "message"]
