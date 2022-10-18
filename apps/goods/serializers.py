from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    DateTimeField,
)

from abstracts.serializers import AbstractDateTimeSerializer
from goods.models import (
    Good,
    Product,
    Parameter,
    GoodParameter,
)
from shops.serializers import (
    ShopGoodModelSerializer,
)


class ParameterBaseModelSerializer(AbstractDateTimeSerializer, ModelSerializer):
    """ParameterBaseModelSerializer."""

    is_deleted: SerializerMethodField = \
        AbstractDateTimeSerializer.is_deleted

    class Meta:
        """Customization of the Serializer."""

        model: Parameter = Parameter
        fields: tuple[str] = (
            "id",
            "name",
            "is_deleted",
        )


class GoodParameterBaseModelSerializer(ModelSerializer):
    """GoodParameterBaseModelSerializer."""

    parameter: ParameterBaseModelSerializer = ParameterBaseModelSerializer()

    class Meta:
        """Customization of the serializer."""

        model: GoodParameter = GoodParameter
        fields: tuple[str] = (
            "good_id",
            "parameter",
            "value",
        )


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
    """ListGoodSerializ ChatMembersListSerailizerer."""

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
    parameters: GoodParameterBaseModelSerializer = \
        GoodParameterBaseModelSerializer(source="goodparameter_set", many=True)
    shops: ShopGoodModelSerializer = ShopGoodModelSerializer(
        source="shopgood_set",
        many=True
    )

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
            "shops",
        )
