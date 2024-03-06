from django.contrib import admin

from blog_system.common.models import BlogSystemSettings


@admin.register(BlogSystemSettings)
class BlogSystemSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
