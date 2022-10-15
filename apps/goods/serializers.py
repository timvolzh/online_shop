from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    DateTimeField,
)

from abstracts.serializers import AbstractDateTimeSerializer
from goods.models import Good, Product


class BaseProductModelSerializer(
    AbstractDateTimeSerializer,
    ModelSerializer
):
    """BaseProductSerializer."""

    is_deleted: SerializerMethodField = \
        AbstractDateTimeSerializer.is_deleted
    datetime_created: DateTimeField = \
        AbstractDateTimeSerializer.datetime_created

    class Meta:
        """Customization of the Serializer."""

        model: Product = Product
        fields: tuple[str] = (
            "name",
            "manufacture",
            "category",
            "datetime_created",
            "is_deleted",
        )


class BaseGoodModelSerializer(
    AbstractDateTimeSerializer,
    ModelSerializer
):
    """ListGoodSerializer."""

    is_deleted: SerializerMethodField = \
        AbstractDateTimeSerializer.is_deleted
    datetime_created: DateTimeField = \
        AbstractDateTimeSerializer.datetime_created

    class Meta:
        """Customization of the Serializer."""

        model: Good = Good
        fields: tuple[str] = (
            "id",
            "name",
            "price_rrc",
            "product",
            "datetime_created",
            "is_deleted",
        )


class ListGoodModelSerializer(BaseGoodModelSerializer):
    """ListGoodModelSerializer."""

    product: BaseProductModelSerializer = BaseProductModelSerializer()


class DetailGoodModelSerializer(BaseGoodModelSerializer):
    """DetailGoodModelSerializer."""

    product: BaseProductModelSerializer = BaseProductModelSerializer()

    class Meta:
        """Customization of the Serializer."""

        model: Good = Good
        fields: tuple[str] = (
            "id",
            "name",
            "price_rrc",
            "product",
            "datetime_created",
            "is_deleted",
            "parameters",
        )
