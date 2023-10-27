from django.urls import path
from .views import ProductViewSet, PedidoViewSet, DetalleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('pedidos', PedidoViewSet, basename='pedidos')
router.register('detalle', DetalleViewSet, basename='detalle')

urlpatterns = router.urls