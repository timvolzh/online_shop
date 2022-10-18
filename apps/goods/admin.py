from django.contrib.admin import (
    ModelAdmin,
    register,
)

from goods.models import (
    Parameter,
    Manufacture,
    Category,
    Product,
    Good,
    GoodParameter,
)


@register(Parameter)
class ParameterAdmin(ModelAdmin):
    """Parameter model admin customization."""

    pass


@register(Manufacture)
class ManufactureAdmin(ModelAdmin):
    """Manufacture db model customization on admin site."""

    pass


@register(Category)
class CategoryAdmin(ModelAdmin):
    """Category db model admin customization."""

    pass


@register(Product)
class ProductAdmin(ModelAdmin):
    """Product db model customization on admin site."""

    pass


@register(Good)
class GoodAdmin(ModelAdmin):
    """Good db model admin customization."""

    pass


@register(GoodParameter)
class GoodParameterAdmin(ModelAdmin):
    """GoodParameterAdmin model on admin site."""

    list_display: tuple[str] = (
        "id",
        "good",
        "parameter",
        "value",
    )
