from typing import Any
from datetime import datetime

from django.db.models import (
    Model,
    DateTimeField,
)


class AbstractDateTime(Model):
    datetime_created: DateTimeField = DateTimeField(
        verbose_name="время и дата создания",
        auto_now_add=True
    )
    datetime_updated: DateTimeField = DateTimeField(
        verbose_name="время и дата обновления",
        auto_now=True
    )
    datetime_deleted: DateTimeField = DateTimeField(
        verbose_name="время и дата удаления",
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def save(self, *args: tuple[Any], **kwargs: dict[str, Any]) -> None:
        super().save(*args, **kwargs)

    def delete(self, *args: tuple[Any], **kwargs: dict[str, Any]) -> None:
        datetime_now: datetime = datetime.now()
        self.datetime_deleted = datetime_now
        self.save(
            update_fields=['datetime_deleted']
        )

# save
# UPDATE abstracts
# SET datetime_created = "",
#     datetime_updated = "",
#     datetime_deleted = "2022-02-22 15:38"
# ...

# save (update_fields=["datetime_deleted"])
# UPDATE abstracts
# SET datetime_deleted = "2022-02-22 15:38"
# ...


# Monkey: def sayHi(self): print("Hi from monkey") a = 5
# Person(Monkey): a = 10 def sayHi(self): print("Hi from Person", super().sayHi(), super().a)

# p: Person = Person()
# p.sayHi()  # Hi from Person Hi from Monkey
