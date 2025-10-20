"""
Common models for the application.
"""

# Django imports
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Django Rest Framework imports

# Third party imports

# Local imports


class IsDeletedManager(models.Manager):
    """
    Manager to filter out soft-deleted objects by default.
    """

    def get_queryset(self):
        """
        Override the default queryset to exclude soft-deleted objects.
        """
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    """
    Tracks instance creations, updates, and (soft) deletions.
    """

    created_by = models.ForeignKey(
        to=User,
        verbose_name=_("Created by"),
        null=True,
        blank=True,
        related_name="%(class)s_created",
        on_delete=models.SET_NULL,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
        editable=False,
        db_index=True,
        null=True,
    )

    updated_by = models.ForeignKey(
        to=User,
        verbose_name=_("Updated by"),
        null=True,
        blank=True,
        related_name="%(class)s_updated",
        on_delete=models.SET_NULL,
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True,
        null=True,
        blank=True,
    )

    deleted_by = models.ForeignKey(
        to=User,
        verbose_name=_("Deleted by"),
        null=True,
        blank=True,
        related_name="%(class)s_deleted",
        on_delete=models.SET_NULL,
    )

    deleted_at = models.DateTimeField(
        verbose_name=_("Deleted at"), null=True, blank=True, default=None
    )

    is_deleted = models.BooleanField(verbose_name=_("Is deleted"), default=False)

    objects = IsDeletedManager()

    objects_all = models.Manager()

    class Meta:
        """
        Abstract base class for all models in the app. Not a real table
        """
        abstract = True
