from typing import (
    Any,
    Optional,
    List,
)

from django.db.models import QuerySet

from rest_framework.request import Request as DRF_Request
from rest_framework.response import Response as DRF_Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status

from orders.models import (
    Order,
    OrderGood,
    STATUS_OK,
)
from orders.serializers import (
    OrderBaseModelSerializer,
    OrderListModelSerializer,
    OrderDetailModelSerializer,
    OrderCreateModelSerializer,
    OrderGoodBaseModelSerializer,
    OrderGoodViewModelSerializer,
)
# from orders.utils import email_changed_order_status
from utils.celery_app import email_changed_order_status
from abstracts.mixins import ModelInstanceMixin
from abstracts.handlers import DRFResponseHandler
from auths.permissions import IsShopManagerOrAdmin
from abstracts.models import AbstractDateTimeQuerySet


class OrderViewSet(ModelInstanceMixin, DRFResponseHandler, ViewSet):
    """OrderViewSet."""

    queryset: AbstractDateTimeQuerySet[Order] = \
        Order.objects.all().select_related(
            "status"
        ).select_related(
            "from_shop"
        ).select_related(
            "orderer"
        )
    serializer_class: OrderBaseModelSerializer = \
        OrderBaseModelSerializer
    permission_classes: tuple[Any] = (IsAuthenticated,)

    def get_queryset(self) -> QuerySet[Order]:
        """Return queryset of not deleted objects."""
        return self.queryset.get_not_deleted()

    def list(
        self,
        request: DRF_Request,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Response:
        """Handle GET-request for all not_deleted orders."""
        response: DRF_Response = self.get_drf_response(
            request=request,
            data=self.get_queryset(),
            serializer_class=OrderListModelSerializer,
            many=True
        )
        return response

    def retrieve(
        self,
        request: DRF_Request,
        pk: int = 0,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Request:
        """Handle GET-request with provided id."""
        is_deleted: bool = request.data.get("is_deleted", False)
        if not is_deleted:
            is_deleted = kwargs.get("is_deleted", False)

        order: Optional[Order] = self.get_queryset_instance_by_id(
            class_name=Order,
            queryset=self.queryset,
            pk=pk,
            is_deleted=is_deleted
        )
        if not order:
            return DRF_Response(
                data={
                    "response": "Данный заказ не найден"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.get_drf_response(
            request=request,
            data=order,
            serializer_class=OrderDetailModelSerializer
        )

    def create(
        self,
        request: DRF_Request,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Response:
        """Handle POST-request for order creation."""
        goods: Optional[list[dict[str, int]]] = request.data.get("goods", None)
        if not goods or not isinstance(goods, list):
            return DRF_Response(
                data={
                    "response": "Список товаров должны быть предоставлены"
                },
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        serializer: OrderCreateModelSerializer = OrderCreateModelSerializer(
            data=request.data,
            context={"request": request}
        )
        valid_data: bool = serializer.is_valid()
        if valid_data:
            new_order: Order = serializer.save()
            response: DRF_Response = self.add_order_goods(
                request,
                new_order,
                goods,
                args,
                kwargs
            )
            return response
        return DRF_Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def add_order_goods(
        self,
        request: DRF_Request,
        order: Order,
        goods: List[dict[str, int]],
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Response:
        """Handle goods to the order."""
        resulted_orders: List[OrderGood] = []

        good: dict[str, int]
        for good in goods:
            if not isinstance(good, dict):
                Order.objects.filter(id=order.id).delete()
                return DRF_Response(
                    data={
                        "response": "Каждый товар в списке не передан в JSON"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            resulted_orders.append(
                OrderGood(
                    order_id=order.id,
                    good_id=good["good"],
                    quantity=good["quantity"],
                    quantity_price=good["quantity_price"]
                )
            )
        OrderGood.objects.bulk_create(resulted_orders)
        return self.get_drf_response(
            request=request,
            data=order,
            serializer_class=OrderDetailModelSerializer
        )

    def update(
        self,
        request: DRF_Request,
        pk: int,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Response:
        """Handle PUT-request method with provided id."""
        is_partial: bool = kwargs.get("is_partial", False)
        order: Optional[Order] = self.get_queryset_instance_by_id(
            class_name=Order,
            queryset=self.queryset,
            pk=pk
        )
        if not order:
            return DRF_Response(
                data={
                    "response": f"Данный заказ с iD {pk} не найден"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        data_copy: dict[str, Any] = request.data.copy()
        change_fields: Optional[dict[str, Any]] = kwargs.get("status", None)
        if change_fields:
            data_copy["status"] = change_fields

        serializer: OrderBaseModelSerializer = self.serializer_class(
            instance=order,
            data=data_copy,
            partial=is_partial
        )
        serializer.is_valid(raise_exception=True)
        updated_order: Order = serializer.save()
        return self.get_drf_response(
            request=request,
            data=updated_order,
            serializer_class=OrderDetailModelSerializer
        )

    def partial_update(
        self,
        request: DRF_Request,
        pk: int,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Response:
        """Handle PATCH method with provided id."""
        kwargs['is_partial'] = True
        return self.update(request, pk, *args, **kwargs)

    @action(
        methods=["patch"],
        detail=True,
        url_path="confirm",
        permission_classes=(
            IsShopManagerOrAdmin,
        )
    )
    def confirm(
        self,
        request: DRF_Request,
        pk: int,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Response:
        """Handle PATCH-request for order confirming."""
        kwargs['is_partial'] = True
        kwargs['status'] = STATUS_OK
        response: DRF_Response = self.update(request, pk, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            order: Order = Order.objects.get(id=pk)
            email_changed_order_status.delay(
                order_id=pk,
                new_status="подтверждён",
                receivers=[request.user.email, order.orderer.email]
            )
        return response


class OrderGoodViewSet(ModelInstanceMixin, DRFResponseHandler, ViewSet):
    """OrderGoodViewSet."""

    serializer_class: OrderGoodBaseModelSerializer = \
        OrderGoodBaseModelSerializer
    permission_classes: tuple[Any] = (IsAuthenticated,)
    queryset: QuerySet[OrderGood] = OrderGood.objects.all()

    @action(
        methods=["get"],
        detail=True,
        url_path="view",
        permission_classes=(
            IsAuthenticated,
        )
    )
    def view_order_goods(
        self,
        request: DRF_Request,
        pk: str,
        *args: tuple[Any],
        **kwargs: dict[str, Any]
    ) -> DRF_Response:
        """Handle custom GET-request to obtain Order goods info."""
        order: Optional[Order] = self.get_queryset_instance_by_id(
            class_name=Order,
            queryset=Order.objects.all(),
            pk=pk
        )
        if not order:
            return DRF_Response(
                data={
                    "response": f"Данный заказ {pk} не найден"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        response: DRF_Response = self.get_drf_response(
            request=request,
            data=self.queryset.filter(order=order).select_related("good"),
            serializer_class=OrderGoodViewModelSerializer,
            many=True
        )
        return response
