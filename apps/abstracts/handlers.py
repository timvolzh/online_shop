from django.db.models import QuerySet

from rest_framework.request import Request as DRF_Request
from rest_framework.response import Response as DRF_Response
from rest_framework.serializers import Serializer
from rest_framework import status


class DRFResponseHandler:
    """Handler for DRF response."""

    def get_drf_response(
        self,
        request: DRF_Request,
        data: QuerySet,
        serializer_class: Serializer,
        many: bool = False
    ) -> DRF_Response:
        """Return DRF response."""
        serializer: Serializer = serializer_class(
            data,
            many=many
        )
        response: DRF_Response = DRF_Response(
            data={
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
        return response
