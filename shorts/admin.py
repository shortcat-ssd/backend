from django.contrib import admin

from shorts.models import Short, ShortView


@admin.register(Short)
class ShortAdmin(admin.ModelAdmin):
    list_display = ("code", "target", "user", "private", "created_at")
    list_filter = ("private", "created_at")
    search_fields = ("code", "target", "label")
    readonly_fields = ("code", "created_at", "updated_at")


@admin.register(ShortView)
class ShortViewAdmin(admin.ModelAdmin):
    list_display = ("short", "created_at")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)
