from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    IntegerField,
    ManyToManyField,
    CASCADE,
)

from goods.models import Good
from shops.models import Shop
from auths.models import CustomUser
from abstracts.models import AbstractDateTime


MAX_NAME_LEN = 254


class Status(AbstractDateTime):
    """Status database table."""

    name: CharField = CharField(
        max_length=MAX_NAME_LEN,
        unique=True,
        verbose_name="Имя статуса"
    )

    def __str__(self) -> str:
        """Override default magic method."""
        return f"{self.name}"

    class Meta:
        """Customization of the Status table."""

        verbose_name: str = "Статус"
        verbose_name_plural: str = "Статусы"
        ordering: tuple[str] = ("-datetime_updated",)


class Order(AbstractDateTime):
    """Order database table."""

    status: ForeignKey = ForeignKey(
        to=Status,
        on_delete=CASCADE,
        default=1,
        related_name="orders",
        verbose_name="Статус"
    )
    total_sum: IntegerField = IntegerField(
        verbose_name="Финальная стоимость"
    )
    from_shop: ForeignKey = ForeignKey(
        to=Shop,
        on_delete=CASCADE,
        related_name="orders",
        verbose_name="Магазин, в котором все куплено"
    )
    orderer: ForeignKey = ForeignKey(
        to=CustomUser,
        on_delete=CASCADE,
        related_name="orders",
        verbose_name="Заказчик"
    )
    goods: ManyToManyField = ManyToManyField(
        to=Good,
        related_name="orders",
        through="OrderGood",
        through_fields=("order", "good"),
        blank=True,
        verbose_name="Товары"
    )

    def __str__(self) -> str:
        """Override defaulr magic method."""
        return f"Заказ #{self.id}"

    class Meta:
        """Customization of the Order table."""

        verbose_name: str = "Заказ"
        verbose_name_plural: str = "Заказы"
        ordering: tuple[str] = ("-datetime_updated",)


class OrderGood(Model):
    """OrderGood database table."""

    UNIT_ITEM = 1

    order: ForeignKey = ForeignKey(
        to=Order,
        on_delete=CASCADE,
        verbose_name="Заказ"
    )
    good: ForeignKey = ForeignKey(
        to=Good,
        on_delete=CASCADE,
        verbose_name="Товар"
    )
    quantity: IntegerField = IntegerField(
        default=UNIT_ITEM,
        verbose_name="Количество"
    )
    quantity_price: IntegerField = IntegerField(
        verbose_name="Стоимость (тенге)"
    )

    class Meta:
        """Customization of the OrderGood table."""

        verbose_name: str = "Товар в заказе"
        verbose_name_plural: str = "Товары в заказах"
