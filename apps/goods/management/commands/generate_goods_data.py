from datetime import datetime
from random import (
    choice,
    randint,
)
from typing import (
    Any,
    Tuple,
    Dict,
)

from django.core.management.base import BaseCommand

from goods.models import (
    Manufacture,
    Parameter,
    Category,
    Product,
    Good,
)
from abstracts.models import AbstractDateTimeQuerySet


class Command(BaseCommand):
    """Custom command for filling up database."""

    MIN_RRC_PRICE = 1000
    MAX_RRC_PRICE = 20000

    def __init__(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        """Call parent constructor."""
        super().__init__(args, kwargs)

    def __get_name(self, model_name: str = "", index: int = 0) -> str:
        return f"{model_name} {index}"

    def __generate_manufactures(self, required_number: int = 0) -> None:
        """Generate manufactures for db."""
        i: int
        for i in range(required_number):
            Manufacture.objects.get_or_create(
                name=self.__get_name(model_name="Производиель", index=i)
            )
        print("Все производители успешно созданы")

    def __generate_parameters(self, required_number: int = 0) -> None:
        """Generate parameters rows for db."""
        i: int
        for i in range(required_number):
            Parameter.objects.get_or_create(
                name=self.__get_name(model_name="Параметр", index=i)
            )
        print("Все параметры успешно созданы")

    def __generate_categories(self, required_number: int = 0) -> None:
        """Generate Category db data."""
        i: int
        for i in range(required_number):
            Category.objects.get_or_create(
                name=self.__get_name(model_name="Категория", index=i)
            )
        print("Все Категории успешно созданы")

    def __generate_products(self, required_number: int = 0) -> None:
        """Generate products data."""
        existed_manufactures_id: AbstractDateTimeQuerySet[int] = \
            Manufacture.objects.all().values_list("id", flat=True)
        existed_categories_id: AbstractDateTimeQuerySet[int] = \
            Category.objects.all().values_list("id", flat=True)

        i: int
        for i in range(required_number):
            manufacture_id: int = choice(existed_manufactures_id)
            category_id: int = choice(existed_categories_id)
            name: str = self.__get_name(model_name="Продукт", index=i)
            Product.objects.get_or_create(
                name=name,
                manufacture_id=manufacture_id,
                category_id=category_id
            )
        print("Все Продукты успешно созданы")

    def __generate_goods(self, required_number: int = 0) -> None:
        existed_products: AbstractDateTimeQuerySet[int] = \
            Product.objects.all().values_list("id", flat=True)
        name: str = ""
        price_rrc: int = randint(self.MIN_RRC_PRICE, self.MAX_RRC_PRICE)

        i: int
        for i in range(required_number):
            name = self.__get_name(model_name="Товар", index=i)
            price_rrc = randint(self.MIN_RRC_PRICE, self.MAX_RRC_PRICE)
            Good.objects.create(
                name=name,
                price_rrc=price_rrc,
                product_id=choice(existed_products)
            )
        print("Все товары успешно созданы")

    def handle(self, *args: Tuple[Any], **options: Dict[str, Any]) -> None:
        """Handle data filling."""
        start_time: datetime = datetime.now()

        # CustomUser data generation
        MANUFACTURES_NUMBER = 50
        PARAMETERS_NUMBER = 65
        CATEGORIES_NUMBER = 70
        PRODUCTS_NUMBER = 100
        GOODS_NUMBER = 200

        self.__generate_manufactures(required_number=MANUFACTURES_NUMBER)
        self.__generate_parameters(required_number=PARAMETERS_NUMBER)
        self.__generate_categories(required_number=CATEGORIES_NUMBER)
        self.__generate_products(required_number=PRODUCTS_NUMBER)
        self.__generate_goods(required_number=GOODS_NUMBER)

        print(
            "Генерация данных составила: {} секунд".format(
                (datetime.now()-start_time).total_seconds()
            )
        )
