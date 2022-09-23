from typing import (
    Union,
    Any,
)

from django.contrib.admin import (
    ModelAdmin,
    register,
)

from contacts.models import Contact


@register(Contact)
class ContactModel(ModelAdmin):
    """Contact model configuration on admin site."""

    readonly_fields: tuple[str] = (
        "datetime_created",
        "datetime_updated",
        "datetime_deleted",
    )
