from django.contrib.admin import (
    ModelAdmin,
    register,
)

from orders.models import (
    Status,
    Order,
    OrderGood,
)


@register(Status)
class StatusAdmin(ModelAdmin):
    """Status db customization on admin site."""

    pass


@register(Order)
class OrderAdmin(ModelAdmin):
    """Order db model customization on admin site."""

    list_display: tuple[str] = (
        "id",
        "status",
        "from_shop",
        "orderer",
        "total_sum",
    )


@register(OrderGood)
class OrderGoodAdmin(ModelAdmin):
    """Order Good db model customization on admin site."""

    list_display: tuple[str] = (
        "order",
        "good",
        "quantity",
        "quantity_price",
    )
