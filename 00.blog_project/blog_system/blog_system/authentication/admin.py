from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from blog_system.authentication.models import Profile

UserModel = get_user_model()
# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)



admin.site.unregister(UserModel)
admin.site.register(UserModel,UserAdmin)
