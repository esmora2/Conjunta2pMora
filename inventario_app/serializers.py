# serializers.py
from rest_framework import serializers
from .models import Categoria, Producto, Cliente, Venta

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def validate_precio(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio debe ser mayor o igual a 0.")
        return value

    def validate_cantidad_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("La cantidad de stock no puede ser negativa.")
        return value


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

    def validate(self, data):
        producto = data['producto']
        cantidad = data['cantidad']
        if producto.cantidad_stock < cantidad:
            raise serializers.ValidationError('Stock insuficiente para esta venta.')
        return data
