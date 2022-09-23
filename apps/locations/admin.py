from typing import (
    Optional,
    Any,
)

from django.contrib.admin import (
    ModelAdmin,
    register,
)
from django.utils.safestring import mark_safe

from locations.models import City
from abstracts.filters import DeletedStateFilter


@register(City)
class CityModel(ModelAdmin):
    """City model configuration on administration site."""

    readonly_fields: tuple[str] = (
        "datetime_created",
        "datetime_updated",
        "datetime_deleted",
    )
    list_display: tuple[str] = (
        "id",
        "name",
        "get_is_deleted",
    )
    list_display_links: tuple[str] = (
        "id",
        "name",
    )
    search_fields: tuple[str] = (
        "id",
        "name",
    )
    list_filter: tuple[Any] = (
        DeletedStateFilter,
    )
    list_per_page: int = 5

    def get_is_deleted(self, obj: Optional[City] = None) -> str:
        """Get is deleted state of object."""
        if obj.datetime_deleted:
            return mark_safe(
                '<p style="color:red; font-weight: bold; font-size: 17px;">\
                    Город удалён</p>'
            )
        return mark_safe(
            '<p style="color: green; font-weight: bold; font-size: 17px;">\
                Город не удалён</p>'
        )
