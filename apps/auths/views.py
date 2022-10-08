from typing import (
    Dict,
    Tuple,
    Any,
)

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

from auths.models import CustomUser
from auths.serializers import CustomUserSerializer


class CustomUserViewSet(ViewSet):
    """CustomUserViewSet."""

    def list(
        self,
        request: DRF_Request,
        *args: Tuple[Any],
        **kwargs: Dict[str, Any]
    ) -> DRF_Response:
        """Handle GET-request."""
        all_users: QuerySet[CustomUser] = CustomUser.objects.all()
        serializer: CustomUserSerializer = CustomUserSerializer(
            instance=all_users,
            many=True
        )
        response: DRF_Response = DRF_Response(
            data={
                "data": serializer.data
            }
        )
        return response
