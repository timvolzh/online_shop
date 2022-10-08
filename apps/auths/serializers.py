from rest_framework.serializers import ModelSerializer

from auths.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    """CustomUserSerializer."""

    class Meta:
        """Customization of the Serializer."""

        model: CustomUser = CustomUser
        fields: str = "__all__"
