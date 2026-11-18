import uuid
from django.db import models


class UUIDModel(models.Model):
    """
    Abstract model providing a UUID primary key.
    Follows the multi-hospital ERD specification.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    Abstract model providing self-updating created_at and updated_at fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TenantModel(UUIDModel, TimeStampedModel):
    """
    Abstract model for all hospital-scoped entities [H].
    Every tenant record belongs to a specific hospital.
    """
    hospital = models.ForeignKey(
        "hospitals.Hospital",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_set",
    )

    class Meta:
        abstract = True

