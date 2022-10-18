from django.core.exceptions import ValidationError


def negative_price_validator(price: int) -> None:
    """Validate negative price."""
    if price < 0:
        raise ValidationError(
            message="Цена не может быть отрицательной",
            code="negative_good_price"
        )


def negative_quantity_validator(quanitity: int) -> None:
    """Validate negative price."""
    if quanitity < 0:
        raise ValidationError(
            message="Количество товара не может быть отрицательной",
            code="negative_good_quantity"
        )
