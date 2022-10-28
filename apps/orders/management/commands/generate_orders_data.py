import names
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
from django.db.models import QuerySet
from goods.models import Good

from orders.models import (
    Order,
    OrderGood,
    Status,
)
from auths.models import CustomUser
from shops.models import Shop


class Command(BaseCommand):
    """Custom command for filling up database."""

    __statuses: tuple[tuple[int, str]] = (
        (1, "В обработке"),
        (2, "Отклонён"),
        (3, "Ок"),
        (4, "Выдан"),
        (5, "В пути"),
    )
    __existed_goods_id: QuerySet[int] = Good.objects.values_list(
        "id",
        flat=True
    )
    MIN_TOTAL_SUM = 0
    MAX_TOTAL_SUM = 10000

    def __init__(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        """Call parent constructor."""
        super().__init__(args, kwargs)

    def __generate_statuses(self) -> None:
        """Generate order statuses."""
        status: tuple[int, str]
        for status in self.__statuses:
            Status.objects.get_or_create(
                id=status[0],
                name=status[1]
            )
        print("Все статусы успешно созданы")

    def __generate_order_goods(self, order_id: int = 1) -> None:
        order_goods_number: int = randint(1, 10)
        good_quantity: int = 0
        good_unit_price: int = 0
        _: int
        for _ in range(order_goods_number):
            good_quantity = randint(1, 100)
            good_unit_price = randint(1000, 10000)
            OrderGood.objects.create(
                order_id=order_id,
                good_id=choice(self.__existed_goods_id),
                quantity=good_quantity,
                quantity_price=good_unit_price*good_quantity
            )
        print(f"Товары для заказа {order_id} созданы")

    def __generate_orders(self, required_number: int = 0) -> None:
        existed_status_id: QuerySet[int] = Status.objects.values_list(
            "id",
            flat=True
        )
        existed_shops_id: QuerySet[int] = Shop.objects.values_list(
            "id",
            flat=True
        )
        existed_users_id: QuerySet[int] = CustomUser.objects.values_list(
            "id",
            flat=True
        )
        orders_count: int = Order.objects.count()
        total_sum: int = 0

        _: int
        for _ in range(required_number):
            total_sum = randint(self.MIN_TOTAL_SUM, self.MAX_TOTAL_SUM)
            orders_count += 1
            Order.objects.create(
                id=orders_count,
                status_id=choice(existed_status_id),
                total_sum=total_sum,
                from_shop_id=choice(existed_shops_id),
                orderer_id=choice(existed_users_id)
            )
            self.__generate_order_goods(order_id=orders_count)
        print("Все заказы успешно созданы")

    def handle(self, *args: Tuple[Any], **options: Dict[str, Any]) -> None:
        """Handle data filling."""
        start_time: datetime = datetime.now()

        # CustomUser data generation
        ORDERS_NUMBER = 50
        self.__generate_statuses()
        self.__generate_orders(required_number=ORDERS_NUMBER)

        print(
            "Генерация данных составила: {} секунд".format(
                (datetime.now()-start_time).total_seconds()
            )
        )
