from typing import (
    Dict,
    Optional,
    Tuple,
    Any,
)

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

from auths.models import CustomUser, CustomUserManager
from auths.serializers import CustomUserSerializer, DetailCustomUserSerializer


class CustomUserViewSet(ViewSet):
    """CustomUserViewSet."""

    queryset: CustomUserManager = CustomUser.objects

    def get_queryset(self) -> QuerySet[CustomUser]:
        """Get not deleted users."""
        return self.queryset.get_not_deleted()

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

    def retrieve(
        self,
        request: DRF_Request,
        pk: str,
        *args: Tuple[Any],
        **kwargs: Dict[str, Any]
    ) -> DRF_Response:
        """Hadnle GET-request with provided id."""
        is_deleted: bool = request.data.get("is_deleted", False)
        if not is_deleted:
            is_deleted = kwargs.get("is_deleted", False)

        custom_user: Optional[CustomUser] = None
        queryset: QuerySet[CustomUser]

        if not is_deleted:
            queryset = self.get_queryset()
        else:
            queryset = self.queryset.get_deleted()
        try:
            custom_user = queryset.get(pk=pk)
        except CustomUser.DoesNotExist:
            return DRF_Response(
                data={
                    "response": "Такого пользователя не существует"
                }
            )
        serializer: DetailCustomUserSerializer = DetailCustomUserSerializer(
            instance=custom_user
        )
        return DRF_Response(
            data={
                "data": serializer.data
            }
        )
