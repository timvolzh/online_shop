from typing import (
    Any,
    Optional,
)

from django.db.models import QuerySet

from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from goods.models import (
    Good,
)
from goods.serializers import (
    BaseGoodModelSerializer,
    ListGoodModelSerializer,
    DetailGoodModelSerializer,
)
from abstracts.models import AbstractDateTimeQuerySet
from abstracts.handlers import DRFResponseHandler
from abstracts.mixins import ModelInstanceMixin


class GoodViewSet(ModelInstanceMixin, DRFResponseHandler, ViewSet):
    """GoodViewSet."""

    queryset: AbstractDateTimeQuerySet[Good] = \
        Good.objects.all().select_related("product")
    serializer_class: BaseGoodModelSerializer = \
        BaseGoodModelSerializer
    permission_classes: tuple[Any] = (AllowAny,)

    def get_queryset(self) -> QuerySet[Good]:
        """Return queryset of not deleted objects."""
        return self.queryset.get_not_deleted()

    def list(
        self,
        request: DRF_Request,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Response:
        """Handle GET-request for all goods."""
        response: DRF_Response = self.get_drf_response(
            request=request,
            data=self.get_queryset(),
            serializer_class=ListGoodModelSerializer,
            many=True
        )
        return response

    def retrieve(
        self,
        request: DRF_Request,
        pk: int = 0,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Response:
        """Handle GET-request with specified PK (ID)."""
        is_deleted: bool = request.data.get("is_deleted", False)
        if not is_deleted:
            is_deleted = kwargs.get("is_deleted", False)

        good: Optional[Good] = self.get_queryset_instance_by_id(
            class_name=Good,
            queryset=self.queryset,
            pk=pk,
            is_deleted=is_deleted
        )
        if not good:
            return DRF_Response(
                data={
                    "response": "Такой товар не найден"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.get_drf_response(
            request=request,
            data=good,
            serializer_class=DetailGoodModelSerializer
        )
