from django.contrib import admin
from .models import User, UserGroup


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'key', 'user_group', 'day_request_count',
                    'minute_request_count', 'latest_request')


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'metering_rate', 'throttling_rate')


admin.site.register(User, UserAdmin)
admin.site.register(UserGroup, UserGroupAdmin)