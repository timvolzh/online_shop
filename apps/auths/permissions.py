from typing import Any

from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)
from rest_framework.request import Request as DRF_Request


class IsShopManagerOrAdmin(BasePermission):
    """Permission for Manager or Admin validation."""

    def has_permission(
        self,
        request: DRF_Request,
        view: Any
    ) -> bool:
        """Return permission for corresponded user."""
        return bool(
            request.user and
            request.user.is_authenticated and
            (request.user.is_staff or request.user.shop)
        )
