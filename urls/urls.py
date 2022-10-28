from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf import settings

from rest_framework.routers import DefaultRouter

from apps.auths.views import CustomUserViewSet
from apps.goods.views import GoodViewSet
from apps.orders.views import (
    OrderViewSet,
    OrderGoodViewSet,
)

urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

# ------------------------------------------
# API Endpoints
#
router: DefaultRouter = DefaultRouter(trailing_slash=False)

router.register('auths/users', CustomUserViewSet)
router.register('goods/goods', GoodViewSet)
router.register('orders/orders', OrderViewSet)
router.register('orders/order_goods', OrderGoodViewSet)

urlpatterns += [
    path(
        "api/v1/",
        include(router.urls)
    ),
]
