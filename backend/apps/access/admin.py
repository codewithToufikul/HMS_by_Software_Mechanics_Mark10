from django.contrib import admin
from .models import Permission, Role, RolePermission, UserRole


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("code", "department", "description")
    list_filter = ("department",)
    search_fields = ("code", "description")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "hospital", "dashboard_type", "is_system")
    list_filter = ("is_system", "hospital")
    search_fields = ("name", "hospital__name")


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ("role", "permission", "hospital")
    list_filter = ("hospital", "role")


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("hospital_user", "role", "hospital")
    list_filter = ("hospital", "role")

