from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.core.models import UUIDModel, TimeStampedModel
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, UUIDModel, TimeStampedModel):
    """
    Global platform user [G] users.
    Identified primarily by email with UUID primary key.
    """
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("suspended", "Suspended"),
    ]

    email = models.EmailField(unique=True, db_index=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, blank=True, null=True)
    is_super_admin = models.BooleanField(
        default=False,
        help_text="Designates whether this user has platform-wide super admin access.",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")

    # Django admin flags
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.full_name} ({self.email})"

