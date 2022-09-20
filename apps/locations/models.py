from django.db.models import CharField

from abstracts.models import AbstractDateTime


class City(AbstractDateTime):
    """City database table."""

    CITY_MAX_NAME = 254
    name: CharField = CharField(
        max_length=CITY_MAX_NAME,
        unique=True,
        db_index=True,
        verbose_name="Наименование города"
    )

    class Meta:
        """Configuration of the table City."""

        verbose_name: str = "Город"
        verbose_name_plural: str = "Города"
        ordering: tuple[str] = ("-datetime_updated",)
