from django.db.models import (
    ForeignKey,
    CharField,
    TextField,
    CASCADE,
)

from abstracts.models import AbstractDateTime
from auths.models import CustomUser
from orders.models import Order
from locations.models import City


class Contact(AbstractDateTime):
    """Contact database model."""

    ADDRESS_LEN = 70
    BUILDIN_LEN = 10
    FLAT_NUMBER = 7

    order: ForeignKey = ForeignKey(
        to=Order,
        on_delete=CASCADE,
        related_name="contacts",
        verbose_name="Заказ"
    )
    reciever: ForeignKey = ForeignKey(
        to=CustomUser,
        on_delete=CASCADE,
        related_name="contacts",
        verbose_name="Получатель"
    )
    city: ForeignKey = ForeignKey(
        to=City,
        on_delete=CASCADE,
        related_name="contacts",
        verbose_name="Город"
    )
    address: CharField = CharField(
        max_length=ADDRESS_LEN,
        verbose_name="Адрес"
    )
    building_number: CharField = CharField(
        max_length=BUILDIN_LEN,
        verbose_name="Номер здания"
    )
    flat_number: CharField = CharField(
        max_length=FLAT_NUMBER,
        blank=True,
        null=True,
        verbose_name="Номер квартиры/комнаты"
    )
    additional_info: TextField = TextField(
        blank=True,
        null=True,
        verbose_name="Дополнительная информация"
    )

    class Meta:
        """Configuration of the database model."""

        verbose_name: str = "Контактная информация"
        verbose_name_plural: str = "Контактная информация"
