from rest_framework import serializers
from .models import Category, Product, StockMovement

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'category', 'supplier', 'description', 'quantity_in_stock', 'price']

class StockMovementSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )
    movement_type = serializers.ChoiceField(choices=StockMovement.MOVEMENT_TYPES)

    class Meta:
        model = StockMovement
        fields = ['id', 'product', 'product_id', 'movement_type', 'quantity', 'timestamp', 'notes']
        read_only_fields = ['timestamp']
