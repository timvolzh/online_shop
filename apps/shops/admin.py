from django.contrib.admin import (
    ModelAdmin,
    register,
)

from shops.models import (
    Shop,
    ShopGood,
)


@register(Shop)
class ShopAdmin(ModelAdmin):
    """Shop db model customization on admin site."""

    pass


@register(ShopGood)
class ShopGoodAdmin(ModelAdmin):
    """ShopGood db model customization on admin site."""

    pass
