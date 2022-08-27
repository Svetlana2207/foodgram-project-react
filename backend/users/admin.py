from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name")
    list_filter = ("username", "email")
