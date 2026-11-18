from django.conf import settings
from django.db import models
from apps.core.models import UUIDModel, TimeStampedModel


class Hospital(UUIDModel, TimeStampedModel):
    """
    Global table [G] hospitals.
    Represents an independent hospital tenant in the multi-hospital platform.
    """
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("suspended", "Suspended"),
    ]

    registration_number = models.CharField(max_length=100, unique=True, db_index=True)
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, default="")
    phone = models.CharField(max_length=50, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    timezone = models.CharField(max_length=50, default="Asia/Dhaka")

    class Meta:
        db_table = "hospitals"
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitals"

    def __str__(self):
        return f"{self.name} ({self.registration_number})"


class Department(UUIDModel, TimeStampedModel):
    """
    Global table [G] departments.
    Master department catalog across all hospitals.
    """
    code = models.CharField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "departments"
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return f"{self.name} ({self.code})"


class HospitalDepartment(UUIDModel):
    """
    Hospital-owned table [H] hospital_departments.
    Links a hospital to its enabled departments.
    """
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name="hospital_departments",
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="hospital_departments",
    )
    is_enabled = models.BooleanField(default=True)
    enabled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "hospital_departments"
        unique_together = ("hospital", "department")
        verbose_name = "Hospital Department"
        verbose_name_plural = "Hospital Departments"

    def __str__(self):
        return f"{self.hospital.name} - {self.department.name}"


class HospitalUser(UUIDModel):
    """
    Hospital-owned table [H] hospital_users.
    Links a platform user to a specific hospital tenant.
    """
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("suspended", "Suspended"),
    ]

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name="hospital_users",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="hospital_memberships",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "hospital_users"
        unique_together = ("hospital", "user")
        verbose_name = "Hospital User"
        verbose_name_plural = "Hospital Users"

    def __str__(self):
        return f"{self.user.full_name} @ {self.hospital.name}"

