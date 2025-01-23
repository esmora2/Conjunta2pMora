from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventario_app.views import (
    CategoriaViewSet, ProductoViewSet, 
    ClienteViewSet, VentaViewSet
)

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]