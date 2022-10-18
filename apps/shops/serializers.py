from rest_framework.serializers import (
    ModelSerializer,
)

from shops.models import (
    Shop,
    ShopGood,
)


class ShopBaseModelSerializer(ModelSerializer):
    """ShopBaseModelSerializer."""

    # is_deleted: SerializerMethodField = \
    #     AbstractDateTimeSerializer.is_deleted
    # datetime_created: DateTimeField = \
    #     AbstractDateTimeSerializer.datetime_created

    class Meta:
        """Settings of the serializer."""

        model: Shop = Shop
        fields: tuple[str] = (
            "id",
            "name",
            "is_active",
            # "is_deleted",
            # "datetime_created",
        )


class ShopGoodModelSerializer(ModelSerializer):
    """ShopGoodModelSerializer."""

    shop: ShopBaseModelSerializer = ShopBaseModelSerializer()

    class Meta:
        """Customization of the Serializer."""

        model: ShopGood = ShopGood
        fields: tuple[str] = (
            "good_id",
            "shop",
            "unit_price",
            "remained_numbee",
        )
