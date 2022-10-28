from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    DateTimeField,
    HiddenField,
    CurrentUserDefault,
)

from orders.models import (
    Order,
    Status,
    OrderGood,
)
from auths.serializers import ForeignCustomUserSerializer
from abstracts.serializers import AbstractDateTimeSerializer
from shops.serializers import ShopBaseModelSerializer
from goods.serializers import BaseGoodModelSerializer


class OrderGoodBaseModelSerializer(ModelSerializer):
    """OrderGoodModelSerializer."""

    class Meta:
        """Customization of the Serializer."""

        model: OrderGood = OrderGood
        fields: tuple[str] = (
            "order",
            "good",
            "quantity",
            "quantity_price",
        )


class StatusBaseModelSerializer(AbstractDateTimeSerializer, ModelSerializer):
    """StatusBaseModelSerializer."""

    is_deleted: SerializerMethodField = \
        AbstractDateTimeSerializer.is_deleted
    datetime_created: DateTimeField = \
        AbstractDateTimeSerializer.datetime_created

    class Meta:
        """Customization of the serializer."""

        model: Status = Status
        fields: tuple[str] = (
            "id",
            "name",
            "is_deleted",
            "datetime_created",
        )


class OrderBaseModelSerializer(AbstractDateTimeSerializer, ModelSerializer):
    """Base Order model Serializer."""

    is_deleted: SerializerMethodField = \
        AbstractDateTimeSerializer.is_deleted
    datetime_created: DateTimeField = \
        AbstractDateTimeSerializer.datetime_created

    class Meta:
        """Customize serializer."""

        model: Order = Order
        fields: tuple[str] = (
            "id",
            "status",
            "total_sum",
            "from_shop",
            "orderer",
            "is_deleted",
            "datetime_created",
        )


class OrderListModelSerializer(OrderBaseModelSerializer):
    """OrderListModelSerializer."""

    status: StatusBaseModelSerializer = StatusBaseModelSerializer()
    orderer: ForeignCustomUserSerializer = ForeignCustomUserSerializer()
    from_shop: ShopBaseModelSerializer = ShopBaseModelSerializer()


class OrderDetailModelSerializer(OrderBaseModelSerializer):
    """OrderDetailModelSerializer."""

    goods: BaseGoodModelSerializer = BaseGoodModelSerializer(
        many=True
    )
    status: StatusBaseModelSerializer = StatusBaseModelSerializer()
    orderer: ForeignCustomUserSerializer = ForeignCustomUserSerializer()
    from_shop: ShopBaseModelSerializer = ShopBaseModelSerializer()

    class Meta:
        """Customization of the Serializer."""

        model: Order = OrderBaseModelSerializer.Meta.model
        fields: tuple[str] = OrderBaseModelSerializer.Meta.fields + ("goods",)


class OrderCreateModelSerializer(OrderBaseModelSerializer):
    """OrderCreateModelSerializer."""

    orderer: HiddenField = HiddenField(default=CurrentUserDefault())


class OrderGoodViewModelSerializer(OrderGoodBaseModelSerializer):
    """OrderGoodViewModelSerializer."""

    good: BaseGoodModelSerializer = BaseGoodModelSerializer()
