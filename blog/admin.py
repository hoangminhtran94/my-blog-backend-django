from django.contrib import admin
from .models import Blog, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_filter = ("owner", "tags", "updated_at")
    list_display = ("title", "owner", "updated_at")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Blog, PostAdmin)

admin.site.register(Tag)
admin.site.register(Comment)
# Register your models here.
