from django.contrib import admin
from .models import Hospital, Department, HospitalDepartment, HospitalUser


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "registration_number", "status", "phone", "email", "timezone")
    list_filter = ("status", "timezone")
    search_fields = ("name", "registration_number", "phone", "email")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(HospitalDepartment)
class HospitalDepartmentAdmin(admin.ModelAdmin):
    list_display = ("hospital", "department", "is_enabled", "enabled_at")
    list_filter = ("is_enabled", "hospital", "department")


@admin.register(HospitalUser)
class HospitalUserAdmin(admin.ModelAdmin):
    list_display = ("user", "hospital", "status", "joined_at")
    list_filter = ("status", "hospital")
    search_fields = ("user__email", "user__full_name", "hospital__name")

