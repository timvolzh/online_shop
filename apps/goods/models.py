from django.db.models import (
    CharField,
    ForeignKey,
    IntegerField,
    CASCADE,  # Удаляет все связанные с ним строки после удаления в основе
    RESTRICT,
)

from abstracts.models import AbstractDateTime

MAX_NAME_LENGTH = 180


class Parameter(AbstractDateTime):
    """Parameters database table."""

    name: CharField = CharField(
        max_length=MAX_NAME_LENGTH,
        db_index=True,
        unique=True,
        verbose_name="параметр"
    )

    class Meta:
        """Database table configuration."""

        verbose_name: str = "Параметр"
        verbose_name_plural: str = "Параметры"
        ordering: tuple[str] = ("-id",)


class Manufacture(AbstractDateTime):
    """Manufactures database table."""

    name: CharField = CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        db_index=True,
        verbose_name="Наименование производителя"
    )

    class Meta:
        """Database table configuration."""

        verbose_name: str = "Производитель"
        verbose_name_plural: str = "Производители"
        ordering: tuple[str] = ("-id",)


class Category(AbstractDateTime):
    """Categories database table."""

    name: CharField = CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        db_index=True,
        verbose_name="Категория",
        help_text="Категория ваших товаров"
    )

    class Meta:
        """Database table configuration."""

        verbose_name: str = "Категория"
        verbose_name_plural: str = "Категории"
        ordering: tuple[str] = ("-id",)


class Product(AbstractDateTime):
    """Products database table."""

    name: CharField = CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        db_index=True,
        verbose_name="Наименование продукта",
        help_text="Наименование продукта производителя (Iphone, Flesh card)"
    )
    manufacture: ForeignKey = ForeignKey(
        to=Manufacture,
        on_delete=CASCADE,
        related_name="products",
        verbose_name="Производитель"
    )
    category: ForeignKey = ForeignKey(
        to=Category,
        on_delete=CASCADE,
        related_name="products",
        verbose_name="Категория"
    )

    class Meta:
        """Database table configuration."""

        verbose_name: str = "Продукт"
        verbose_name_plural: str = "Продукты"
        ordering: tuple[str] = ("-id",)


class Good(AbstractDateTime):
    """Goods database table."""

    name: CharField = CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name="Наименование товара"
    )
    price_rrc: IntegerField = IntegerField(
        verbose_name="Рекомендованая розничная цена"
    )
    product: ForeignKey = ForeignKey(
        to=Product,
        on_delete=CASCADE
    )

    class Meta:
        """Database table configuration."""

        verbose_name: str = "Товар"
        verbose_name_plural: str = "Товары"
        ordering: tuple[str] = ("-id",)
