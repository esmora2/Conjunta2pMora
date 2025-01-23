from rest_framework import viewsets, status
from django.db.models import Sum
from django.db import transaction
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Categoria, Producto, Cliente, Venta
from .serializers import (CategoriaSerializer, ProductoSerializer, 
                         ClienteSerializer, VentaSerializer)

class CategoriaViewSet(viewsets.ModelViewSet):
   queryset = Categoria.objects.all()
   serializer_class = CategoriaSerializer

   @action(detail=False, methods=['get'])
   def list_with_products(self, request):
       categorias = Categoria.objects.prefetch_related('producto_set').all()
       serializer = self.get_serializer(categorias, many=True)
       return Response(serializer.data)

   def create(self, request):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       self.perform_create(serializer)
       return Response(serializer.data, status=status.HTTP_201_CREATED)

   def update(self, request, *args, **kwargs):
       partial = kwargs.pop('partial', False)
       instance = self.get_object()
       serializer = self.get_serializer(instance, data=request.data, partial=partial)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)
       return Response(serializer.data)

   def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       try:
           self.perform_destroy(instance)
           return Response(status=status.HTTP_204_NO_CONTENT)
       except Exception as e:
           return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProductoViewSet(viewsets.ModelViewSet):
   queryset = Producto.objects.all()
   serializer_class = ProductoSerializer

   def create(self, request):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       self.perform_create(serializer)
       return Response(serializer.data, status=status.HTTP_201_CREATED)

   def update(self, request, *args, **kwargs):
       partial = kwargs.pop('partial', False)
       instance = self.get_object()
       serializer = self.get_serializer(instance, data=request.data, partial=partial)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)
       return Response(serializer.data)

   def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       try:
           self.perform_destroy(instance)
           return Response(status=status.HTTP_204_NO_CONTENT)
       except Exception as e:
           return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

   @action(detail=True, methods=['patch'])
   def update_stock(self, request, pk=None):
        producto = self.get_object()
        try:
            cantidad_stock = int(request.data.get('cantidad_stock'))
            if cantidad_stock < 0:
                return Response({'error': 'cantidad_stock must be non-negative'}, status=status.HTTP_400_BAD_REQUEST)
            producto.cantidad_stock = cantidad_stock
            producto.save()
            return Response({'status': 'stock updated'}, status=status.HTTP_200_OK)
        except (ValueError, TypeError):
            return Response({'error': 'Invalid cantidad_stock value'}, status=status.HTTP_400_BAD_REQUEST)
   

class ClienteViewSet(viewsets.ModelViewSet):
   queryset = Cliente.objects.all()
   serializer_class = ClienteSerializer

   def create(self, request):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       self.perform_create(serializer)
       return Response(serializer.data, status=status.HTTP_201_CREATED)

   def update(self, request, *args, **kwargs):
       partial = kwargs.pop('partial', False)
       instance = self.get_object()
       serializer = self.get_serializer(instance, data=request.data, partial=partial)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)
       return Response(serializer.data)

   def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       try:
           self.perform_destroy(instance)
           return Response(status=status.HTTP_204_NO_CONTENT)
       except Exception as e:
           return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class VentaViewSet(viewsets.ModelViewSet):
   queryset = Venta.objects.all()
   serializer_class = VentaSerializer

   def create(self, request):
    with transaction.atomic():
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        producto = serializer.validated_data['producto']
        cantidad = serializer.validated_data['cantidad']
        
        if producto.cantidad_stock < cantidad:
            return Response({'error': 'Insufficient stock'}, status=status.HTTP_400_BAD_REQUEST)

        producto.cantidad_stock -= cantidad
        producto.save()

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

   def update(self, request, *args, **kwargs):
       partial = kwargs.pop('partial', False)
       instance = self.get_object()
       serializer = self.get_serializer(instance, data=request.data, partial=partial)
       serializer.is_valid(raise_exception=True)
       self.perform_update(serializer)
       return Response(serializer.data)

   def destroy(self, request, *args, **kwargs):
       instance = self.get_object()
       try:
           self.perform_destroy(instance)
           return Response(status=status.HTTP_204_NO_CONTENT)
       except Exception as e:
           return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

   @action(detail=False, methods=['get'])
   def ventas_por_producto(self, request):
    ventas = Venta.objects.values('producto__nombre').annotate(total_ventas=Sum('cantidad'))
    return Response(ventas)