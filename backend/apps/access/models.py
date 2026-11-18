from django.db import models
from apps.core.models import UUIDModel, TimeStampedModel, TenantModel


class Permission(UUIDModel, TimeStampedModel):
    """
    Global table [G] permissions.
    System-wide permission definitions.
    Optionally scoped to a department.
    """
    department = models.ForeignKey(
        "hospitals.Department",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="permissions",
    )
    code = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True, default="")

    class Meta:
        db_table = "permissions"
        verbose_name = "Permission"
        verbose_name_plural = "Permissions"

    def __str__(self):
        return self.code


class Role(TenantModel):
    """
    Hospital-owned table [H] roles.
    Defines roles within a hospital (e.g., Doctor, Nurse, Cashier, Receptionist).
    """
    name = models.CharField(max_length=100)
    dashboard_type = models.CharField(max_length=50, blank=True, default="")
    is_system = models.BooleanField(
        default=False,
        help_text="System-defined roles cannot be deleted.",
    )

    class Meta:
        db_table = "roles"
        unique_together = ("hospital", "name")
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return f"{self.name} ({self.hospital.name})"


class RolePermission(UUIDModel, TimeStampedModel):
    """
    Hospital-owned junction table [H] role_permissions.
    Assigns permissions to a role within a hospital.
    """
    hospital = models.ForeignKey(
        "hospitals.Hospital",
        on_delete=models.CASCADE,
        related_name="role_permissions",
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="role_permissions",
    )
    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        related_name="role_permissions",
    )

    class Meta:
        db_table = "role_permissions"
        unique_together = ("role", "permission")
        verbose_name = "Role Permission"
        verbose_name_plural = "Role Permissions"

    def __str__(self):
        return f"{self.role.name} -> {self.permission.code}"


class UserRole(UUIDModel, TimeStampedModel):
    """
    Hospital-owned junction table [H] user_roles.
    Assigns a role to a hospital user.
    """
    hospital = models.ForeignKey(
        "hospitals.Hospital",
        on_delete=models.CASCADE,
        related_name="user_roles",
    )
    hospital_user = models.ForeignKey(
        "hospitals.HospitalUser",
        on_delete=models.CASCADE,
        related_name="user_roles",
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="user_roles",
    )

    class Meta:
        db_table = "user_roles"
        unique_together = ("hospital_user", "role")
        verbose_name = "User Role"
        verbose_name_plural = "User Roles"

    def __str__(self):
        return f"{self.hospital_user} - {self.role.name}"

