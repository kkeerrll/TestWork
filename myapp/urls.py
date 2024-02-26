from django.urls import include, path
from rest_framework import routers
from .views import SupplierViewSet, NetworkObjectViewSet

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'network-objects', NetworkObjectViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
